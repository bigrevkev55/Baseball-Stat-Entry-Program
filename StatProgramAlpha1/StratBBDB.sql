
--Author:  Kevin Thomas
--Date:    11/2022 (aprox)
--Purpose: Used to create original tables of the StratBB DATABASE
--Noe:     ***VIP*** Some of these tables were altered after original creation so it may be best to get the 
--                   sql of the entire database from SQL Server where the database is stored.  



--drop database "StratBB";

if not exists (select name from master.dbo.sysdatabases where name = 'StratBB') create DATABASE StratBB


create table positions(
    positions_primary_position_code VARCHAR (255) not null PRIMARY KEY,
    positions_position_code_desc VARCHAR (255)
)

create table teams(
    teams_teamID int not null identity PRIMARY KEY, 
	teams_team_season int not null,
	teams_teamabrv VARCHAR(255), 
    teams_teammascot VARCHAR(255)
)

create table projects(
	projects_projectID int identity primary key,
    projects_project_desc VARCHAR(255),
)

create table players (
    players_playerID int not null identity,
	players_player_season int not null,
    players_player_last varchar (255), 
    players_player_first varchar (255),
    players_player_primary_position VARCHAR(255) Foreign KEY REFERENCES positions(positions_primary_position_code) NOT NULL, 
	players_player_teamID int FOREIGN KEY REFERENCES teams(teams_teamID) NOT NULL,
	players_player_team_season int not null,
	primary key(players_playerID, players_player_season)
)

create table game_details(
    game_details_gameID int not null identity PRIMARY KEY,
    game_details_projectID int FOREIGN KEY REFERENCES projects(projects_projectID) NOT NULL,
    game_details_home_team int FOREIGN KEY REFERENCES teams(teams_teamid) NOT NULL,
    game_details_visiting_team int FOREIGN KEY REFERENCES teams(teams_teamID) NOT NULL,
    game_details_winning_team int FOREIGN KEY REFERENCES teams(teams_teamid) NOT NULL,
    game_details_info_losing_team int FOREIGN KEY REFERENCES teams(teams_teamid) NOT NULL
)


create table player_games(
    player_games_playerID int FOREIGN KEY REFERENCES players(players_playerID) NOT NULL,
    player_games_gameID int FOREIGN KEY REFERENCES game_details (game_details_gameID) NOT NULL,
	player_games_game_appearance bit NOT NULL Default 1, --1 if appeared in game, 0 if didn't appear in game
	player_games_ABs int, 
	player_games_hitting_walks int,
	player_games_hitting_HBP int,
	player_games_hitting_strikeouts int,
	player_games_hitting_runs int,
	player_games_hitting_hits int,
	player_games_hitting_doubles int,
	player_games_hitting_triples int,
	player_games_hitting_homeruns int,
	player_games_hitting_RBIs int,
	player_games_hitting_sacrificess int, 
	player_games_hitting_SB int,
	player_games_hitting_SB_attempts int,
	player_games_fielding_errors int,
	player_games_pitching_IP int,
	player_games__win int,
	player_games_loss int,
	player_games_hold int,
	player_games_save int,
	player_games_hits_allowed int,
	player_games_pitching_BBs int,
	player_games_pitching_strikeouts int,
	player_games_pitching_HBP int,
	player_games_pitching_homeruns_allowed int,
	player_games_pitching_runs_allowed int,
	player_games_pitching_earned_runs_allowed int, 
	player_games_pitching_complete_game int,
	player_games_pitching_shutout int, 
	player_games_pitching_wild_pitch int,
	player_games_pitching_balk int,
	primary key(player_games_playerID, player_games_gameID)
);

