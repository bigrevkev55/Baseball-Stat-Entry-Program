

#Creates the SQLite DB and exposes get_connection()


import sqlite3
import os

DB_FILE = "stratbb.db"

def get_connection():
    """Return a connection to the SQLite database with FK support enabled."""
    conn = sqlite3.connect(DB_FILE)
    conn.execute("PRAGMA foreign_keys = ON;")
    return conn


def initialize_database():
    """Create the SQLite database and tables if they do not already exist."""
    if os.path.exists(DB_FILE):
        print('Connected to Stratbb.db')
        return  # DB already exists — nothing to do

    conn = get_connection()
    c = conn.cursor()

    # -----------------------------
    # TABLE CREATION
    # -----------------------------
    schema = """
    PRAGMA foreign_keys = ON;

    CREATE TABLE positions (
        positions_primary_position_code TEXT PRIMARY KEY,
        positions_position_code_desc TEXT
    );

    CREATE TABLE teams (
        teams_teamID INTEGER PRIMARY KEY AUTOINCREMENT,
        teams_team_season INTEGER NOT NULL,
        teams_teamabrv TEXT,
        teams_teammascot TEXT
    );

    CREATE TABLE projects (
        projects_projectID INTEGER PRIMARY KEY AUTOINCREMENT,
        projects_project_desc TEXT
    );

    CREATE TABLE players (
        players_playerID INTEGER PRIMARY KEY AUTOINCREMENT,
        players_player_season INTEGER NOT NULL,
        players_player_last TEXT,
        players_player_first TEXT,
        players_player_primary_position TEXT NOT NULL,
        players_player_teamID INTEGER NOT NULL,
        players_player_team_season INTEGER NOT NULL,
        FOREIGN KEY (players_player_primary_position)
            REFERENCES positions(positions_primary_position_code),
        FOREIGN KEY (players_player_teamID)
            REFERENCES teams(teams_teamID)
    );

    CREATE TABLE game_details (
        game_details_gameID INTEGER PRIMARY KEY AUTOINCREMENT,
        game_details_projectID INTEGER NOT NULL,
        game_details_home_team INTEGER NOT NULL,
        game_details_visiting_team INTEGER NOT NULL,
        game_details_winning_team INTEGER NOT NULL,
        game_details_info_losing_team INTEGER NOT NULL,
        game_details_start_time TEXT,
        game_details_end_time TEXT,
        game_details_game_date TEXT,
        FOREIGN KEY (game_details_projectID)
            REFERENCES projects(projects_projectID),
        FOREIGN KEY (game_details_home_team)
            REFERENCES teams(teams_teamID),
        FOREIGN KEY (game_details_visiting_team)
            REFERENCES teams(teams_teamID),
        FOREIGN KEY (game_details_winning_team)
            REFERENCES teams(teams_teamID),
        FOREIGN KEY (game_details_info_losing_team)
            REFERENCES teams(teams_teamID)
    );

    CREATE TABLE player_games (
        player_games_playerID INTEGER NOT NULL,
        player_games_gameID INTEGER NOT NULL,
        player_games_game_appearance INTEGER NOT NULL DEFAULT 1,
        player_games_ABs INTEGER,
        player_games_hitting_walks INTEGER,
        player_games_hitting_HBP INTEGER,
        player_games_hitting_strikeouts INTEGER,
        player_games_hitting_runs INTEGER,
        player_games_hitting_hits INTEGER,
        player_games_hitting_doubles INTEGER,
        player_games_hitting_triples INTEGER,
        player_games_hitting_homeruns INTEGER,
        player_games_hitting_RBIs INTEGER,
        player_games_hitting_sacrificess INTEGER,
        player_games_hitting_SB INTEGER,
        player_games_hitting_SB_attempts INTEGER,
        player_games_fielding_errors INTEGER,
        player_games__win INTEGER,
        player_games_loss INTEGER,
        player_games_hold INTEGER,
        player_games_save INTEGER,
        player_games_hits_allowed INTEGER,
        player_games_pitching_BBs INTEGER,
        player_games_pitching_strikeouts INTEGER,
        player_games_pitching_HBP INTEGER,
        player_games_pitching_homeruns_allowed INTEGER,
        player_games_pitching_runs_allowed INTEGER,
        player_games_pitching_earned_runs_allowed INTEGER,
        player_games_pitching_complete_game INTEGER,
        player_games_pitching_shutout INTEGER,
        player_games_pitching_wild_pitch INTEGER,
        player_games_pitching_balk INTEGER,
        player_games_pitching_innings_pitched REAL,
        PRIMARY KEY (player_games_playerID, player_games_gameID),
        FOREIGN KEY (player_games_playerID)
            REFERENCES players(players_playerID),
        FOREIGN KEY (player_games_gameID)
            REFERENCES game_details(game_details_gameID)
    );
    """

    c.executescript(schema)

    # -----------------------------
    # VIEW CREATION
    # -----------------------------
    views = """
    CREATE VIEW braves_record AS
    SELECT
        '1996 Braves' AS Team,
        (SELECT COUNT(game_details_winning_team)
         FROM game_details
         WHERE game_details_winning_team = 1
           AND game_details_projectID = 1) AS Won,
        (SELECT COUNT(game_details_info_losing_team)
         FROM game_details
         WHERE game_details_info_losing_team = 1
           AND game_details_projectID = 1) AS Lost;

    CREATE VIEW hitting_stats AS
    SELECT
        players.players_player_last AS Last,
        players.players_player_first AS First,
        COUNT(player_games_gameID) AS Games_Played,
        CASE
            WHEN SUM(player_games_ABs) = 0 THEN 0
            ELSE ROUND(CAST(SUM(player_games_hitting_hits) AS REAL) / SUM(player_games_ABs), 3)
        END AS Batting_Average,
        CASE
            WHEN (SUM(player_games_ABs) +
                  SUM(player_games_hitting_walks) +
                  SUM(player_games_hitting_HBP)) = 0 THEN 0
            ELSE ROUND(
                CAST(
                    SUM(
                        player_games_hitting_hits +
                        player_games_hitting_walks +
                        player_games_hitting_HBP
                    ) AS REAL
                ) /
                (SUM(player_games_ABs) +
                 SUM(player_games_hitting_walks) +
                 SUM(player_games_hitting_HBP)),
                3
            )
        END AS On_Base_Percentage,
        CASE
            WHEN SUM(player_games_ABs) = 0 THEN 0
            ELSE ROUND(
                CAST(
                    SUM(
                        player_games_hitting_hits +
                        player_games_hitting_doubles +
                        2 * player_games_hitting_triples +
                        3 * player_games_hitting_homeruns
                    ) AS REAL
                ) /
                SUM(player_games_ABs),
                3
            )
        END AS Slugging_Percentage,
        SUM(player_games_hitting_hits) AS Hits,
        SUM(player_games_ABs) AS ABs,
        SUM(player_games_hitting_walks) AS Walks,
        SUM(player_games_hitting_HBP) AS HBP,
        SUM(player_games_hitting_strikeouts) AS Strikeouts,
        SUM(player_games_hitting_runs) AS Runs,
        SUM(player_games_hitting_doubles) AS Doubles,
        SUM(player_games_hitting_triples) AS Triples,
        SUM(player_games_hitting_homeruns) AS Homeruns,
        SUM(player_games_hitting_RBIs) AS RBIs,
        SUM(player_games_hitting_SB) AS SBs,
        SUM(player_games_fielding_errors) AS Errors
    FROM player_games
    INNER JOIN players ON players.players_playerID = player_games.player_games_playerID
    GROUP BY players.players_player_last, players.players_player_first;

    CREATE VIEW last_game_entered AS
    SELECT *
    FROM player_games
    WHERE player_games_gameID = (
        SELECT MAX(player_games_gameID)
        FROM player_games
    );

    CREATE VIEW last_game_boxscore AS
    SELECT  
        l.player_games_gameID AS Game,
        p.players_player_last AS Last,
        p.players_player_first AS First,
        l.player_games_hitting_hits AS Hits,
        l.player_games_ABs AS At_Bats,
        l.player_games_hitting_doubles AS Doubles,
        l.player_games_hitting_triples AS Triples,
        l.player_games_hitting_homeruns AS Homeruns,
        l.player_games_hitting_RBIs AS RBIs,
        l.player_games_hitting_walks AS Walks,
        l.player_games_hitting_strikeouts AS Strikeouts,
        l.player_games_hitting_SB AS Steals
    FROM players p
    JOIN last_game_entered l 
        ON p.players_playerID = l.player_games_playerID
    JOIN game_details g 
        ON g.game_details_gameID = l.player_games_gameID;

    CREATE VIEW pitchers AS
    SELECT  
        players.players_player_season AS Season,
        players.players_player_first AS First,
        players.players_player_last AS Last,
        positions.positions_position_code_desc AS Position
    FROM players
    INNER JOIN positions 
        ON positions.positions_primary_position_code = players.players_player_primary_position
    WHERE players.players_player_primary_position = '1';

    CREATE VIEW pitching_stats AS
    SELECT
        players_playerID AS ID,
        players_player_last AS Last,
        players_player_first AS First,
        COUNT(player_games.player_games_game_appearance) AS Appearances,
        '' AS Starts,
        SUM(player_games.player_games__win) AS Wins,
        SUM(player_games.player_games_loss) AS Losses,
        SUM(player_games.player_games_save) AS Saves,
        CASE
            WHEN SUM(player_games_pitching_innings_pitched) > 0
                THEN ROUND(
                    (SUM(player_games_pitching_BBs) + SUM(player_games_hits_allowed)) /
                    SUM(player_games_pitching_innings_pitched),
                    2
                )
            ELSE NULL
        END AS WHIP,
        CASE
            WHEN SUM(player_games_pitching_innings_pitched) > 0
                THEN ROUND(
                    (9 * SUM(player_games_pitching_earned_runs_allowed)) /
                    SUM(player_games_pitching_innings_pitched),
                    2
                )
            ELSE NULL
        END AS ERA,
        ROUND(SUM(player_games_pitching_innings_pitched), 1) AS IP,
        SUM(player_games_hits_allowed) AS Hits,
        SUM(player_games_pitching_BBs) AS BBs,
        SUM(player_games_pitching_strikeouts) AS Ks,
        SUM(player_games_pitching_HBP) AS HBP,
        SUM(player_games_pitching_homeruns_allowed) AS HRA,
        SUM(player_games_pitching_runs_allowed) AS Runs,
        SUM(player_games_pitching_earned_runs_allowed) AS Earned_Runs,
        SUM(player_games_pitching_complete_game) AS Complete_Games,
        SUM(player_games_pitching_shutout) AS Shutouts,
        SUM(player_games_pitching_wild_pitch) AS WP,
        SUM(player_games_pitching_balk) AS BK
    FROM player_games
    INNER JOIN players 
        ON players.players_playerID = player_games.player_games_playerID
    WHERE players.players_player_primary_position = '1'
    GROUP BY players_playerID, players_player_last, players_player_first;

    CREATE VIEW team_v_team AS
    WITH OpposingTeams AS (
        SELECT
            CASE
                WHEN gd.game_details_home_team = 1 
                    THEN gd.game_details_visiting_team
                ELSE gd.game_details_home_team
            END AS opposing_team,
            game_details_winning_team,
            game_details_info_losing_team
        FROM game_details gd
        WHERE game_details_home_team = 1 
           OR game_details_visiting_team = 1
    )
    SELECT
        opposing_team AS Opponent_Team_ID,
        teams.teams_teammascot AS Opponent_Mascot,
        COUNT(*) AS Games_Played,
        SUM(CASE WHEN game_details_winning_team = 1 THEN 1 ELSE 0 END) AS Wins,
        SUM(CASE WHEN game_details_info_losing_team = 1 THEN 1 ELSE 0 END) AS Losses
    FROM OpposingTeams
    INNER JOIN teams 
        ON teams.teams_teamID = opposing_team
    GROUP BY opposing_team, teams.teams_teammascot;
    """

    c.executescript(views)
    conn.commit()
    conn.close()

    print("SQLite database created successfully: stratbb.db")


# Run initialization automatically when this module is imported
initialize_database()
