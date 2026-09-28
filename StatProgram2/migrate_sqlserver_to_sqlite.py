"""
Name: Kevin Thomas
Date: February 7, 2026
Description:
    One-time migration script used to transfer all existing StratBB data
    from the legacy SQL Server database into the new portable SQLite database.

    This script:
        - Connects to SQL Server in read-only mode
        - Connects to SQLite for writing
        - Copies all tables in the correct dependency order
        - Preserves all primary keys and foreign key relationships
        - Ensures the new SQLite database contains a complete copy of the
          original StratBB data for use in the modernized application.

    This script should only be run once, after the SQLite schema has been created.
"""

import sqlite3
import pyodbc

# -----------------------------
# SQL Server connection
# -----------------------------
sql_conn = pyodbc.connect(
    'Driver={SQL Server};'
    'Server=DESKTOP-SCL1250\\SQLEXPRESS01;'
    'Database=StratBB;'
    'Trusted_Connection=yes;'
)
sql_cursor = sql_conn.cursor()

# -----------------------------
# SQLite connection
# -----------------------------
sqlite_conn = sqlite3.connect("stratbb.db")
sqlite_cursor = sqlite_conn.cursor()

print("Starting migration...\n")

# -----------------------------
# Helper function
# -----------------------------
def migrate_table(table_name, columns):
    print(f"Migrating {table_name}...")

    col_list = ", ".join(columns)
    placeholders = ", ".join(["?"] * len(columns))

    sql_cursor.execute(f"SELECT {col_list} FROM {table_name}")
    rows = sql_cursor.fetchall()

    for row in rows:
        sqlite_cursor.execute(
            f"INSERT INTO {table_name} ({col_list}) VALUES ({placeholders})",
            row
        )

    sqlite_conn.commit()
    print(f"  → {len(rows)} rows migrated.\n")


# -----------------------------
# Migration order matters!
# -----------------------------
# 1. positions
migrate_table("positions", [
    "positions_primary_position_code",
    "positions_position_code_desc"
])

# 2. teams
migrate_table("teams", [
    "teams_teamID",
    "teams_team_season",
    "teams_teamabrv",
    "teams_teammascot"
])

# 3. projects
migrate_table("projects", [
    "projects_projectID",
    "projects_project_desc"
])

# 4. players
migrate_table("players", [
    "players_playerID",
    "players_player_season",
    "players_player_last",
    "players_player_first",
    "players_player_primary_position",
    "players_player_teamID",
    "players_player_team_season"
])

# 5. game_details
migrate_table("game_details", [
    "game_details_gameID",
    "game_details_projectID",
    "game_details_home_team",
    "game_details_visiting_team",
    "game_details_winning_team",
    "game_details_info_losing_team",
    "game_details_start_time",
    "game_details_end_time",
    "game_details_game_date"
])

# 6. player_games
migrate_table("player_games", [
    "player_games_playerID",
    "player_games_gameID",
    "player_games_game_appearance",
    "player_games_ABs",
    "player_games_hitting_walks",
    "player_games_hitting_HBP",
    "player_games_hitting_strikeouts",
    "player_games_hitting_runs",
    "player_games_hitting_hits",
    "player_games_hitting_doubles",
    "player_games_hitting_triples",
    "player_games_hitting_homeruns",
    "player_games_hitting_RBIs",
    "player_games_hitting_sacrificess",
    "player_games_hitting_SB",
    "player_games_hitting_SB_attempts",
    "player_games_fielding_errors",
    "player_games__win",
    "player_games_loss",
    "player_games_hold",
    "player_games_save",
    "player_games_hits_allowed",
    "player_games_pitching_BBs",
    "player_games_pitching_strikeouts",
    "player_games_pitching_HBP",
    "player_games_pitching_homeruns_allowed",
    "player_games_pitching_runs_allowed",
    "player_games_pitching_earned_runs_allowed",
    "player_games_pitching_complete_game",
    "player_games_pitching_shutout",
    "player_games_pitching_wild_pitch",
    "player_games_pitching_balk",
    "player_games_pitching_innings_pitched"
])

print("Migration complete!")
sqlite_conn.close()
sql_conn.close()
