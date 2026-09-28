--see stats entered from max game
Select * from player_games where player_games_gameid = (select max(player_games_gameId) from player_games);

--96 Braves Linescores
DROP SEQUENCE game_number 
DROP SEQUENCE Wins
DROP SEQUENCE Losses

CREATE SEQUENCE game_number as INT
                start with 1
				INCREMENT BY 1

CREATE SEQUENCE Wins as INT
				start with 1
				INCREMENT BY 1

CREATE SEQUENCE Losses as INT
			  start with 1
			  INCREMENT by 1

SELECT NEXT VALUE FOR game_number over (order by game_details_gameID) as "Game Number",
	   v.teams_teamabrv + ' ' + v.teams_teammascot as " Visiting Team",
	   h.teams_teamabrv + ' ' + h.teams_teammascot as "Home Team",
	   w.teams_teamabrv + ' ' + w.teams_teammascot as "Winner",
	   CASE when game_details_winning_team = 1 then 1 end as "Wins",
	   CASE when game_details_winning_team != 1 then 1  end as "Losses"
from game_details
inner join teams w on game_details_winning_team = w.teams_teamID
inner join teams v on game_details_visiting_team = v.teams_teamID
inner join teams h on game_details_home_team = h.teams_teamID;

--Braves Record
select '1996 Braves' as Team,
       (select count(game_details_winning_team) from game_details where game_details_winning_team='1' and game_details_projectID='1') as "Won",
       (select count(game_details_info_losing_team) from game_details where game_details_info_losing_team='1' and game_details_projectID='1') as "Lost";

--Pitchers in Project
select  players_player_season as "Season",
		players_player_first First,
		players_player_last Last,
       positions_position_code_desc as "Position"
from players
inner join positions on positions_primary_position_code = players_player_primary_position
where players_player_primary_position =1;


--Batting Stats for players that have at least one Plate Appearance
SELECT
    players.players_player_last AS "Last",
    players.players_player_first AS "First",
    COUNT(player_games_gameID) AS "Games Played",
    CAST(
        CASE
            WHEN SUM(player_games_ABs) = 0 THEN 0
            ELSE ROUND(CAST(SUM(player_games_hitting_hits) AS DECIMAL) / SUM(player_games_ABs), 3)
        END AS DECIMAL(10, 3)
    ) AS "Batting Average",
    CAST(
        CASE
            WHEN (SUM(player_games_ABs) + SUM(player_games_hitting_walks) + SUM(player_games_hitting_HBP)) = 0 THEN 0
            ELSE ROUND(
                CAST(SUM(player_games_hitting_hits + player_games_hitting_walks + player_games_hitting_HBP) AS DECIMAL) /
                (SUM(player_games_ABs) + SUM(player_games_hitting_walks) + SUM(player_games_hitting_HBP)),
                3
            )
        END AS DECIMAL(10, 3)
    ) AS "On Base %",
    CAST(
        CASE
            WHEN SUM(player_games_ABs) = 0 THEN 0
            ELSE ROUND(
                CAST(SUM(player_games_hitting_hits + player_games_hitting_doubles + 2 * player_games_hitting_triples + 3 * player_games_hitting_homeruns) AS DECIMAL) /
                SUM(player_games_ABs),
                3
            )
        END AS DECIMAL(10, 3)
    ) AS "Slugging %",
    SUM(player_games_hitting_hits) AS "Hits",
    SUM(player_games_ABs) AS "ABs",
    SUM(player_games_hitting_walks) AS "Walks",
    SUM(player_games_hitting_HBP) AS "HBP",
    SUM(player_games_hitting_strikeouts) AS "Strikeouts",
    SUM(player_games_hitting_runs) AS "Runs",
    SUM(player_games_hitting_doubles) AS "Doubles",
    SUM(player_games_hitting_triples) AS "Triples",
    SUM(player_games_hitting_homeruns) AS "Homeruns",
    SUM(player_games_hitting_RBIs) AS RBIs,
    SUM(player_games_hitting_SB) AS "SBs",
    SUM(player_games_fielding_errors) AS "Errors"
FROM player_games
INNER JOIN players ON players.players_playerid = player_games.player_games_playerid
GROUP BY players.players_player_last, players.players_player_first
ORDER BY players.players_player_last, players.players_player_first;



--Pitching Stats for players that have their position listed as SP or RP
SELECT 
	players_playerID AS ID,
	players_player_last AS Last,
    players_player_first AS First,
    COUNT(player_games.player_games_game_appearance) AS Appearances,
	'' as "Starts",
	SUM(player_games.player_games__win) as "Wins",
	SUM(player_games.player_games_loss) as "Losses",
	SUM(Player_games.player_games_save) as "Saves",
    CASE
        WHEN SUM(player_games_pitching_innings_pitched) > 0
            THEN Round((SUM(player_games_pitching_BBs) + SUM(player_games_hits_allowed)) / SUM(player_games_pitching_innings_pitched),2)
            ELSE NULL
    END AS WHIP,
    CASE
        WHEN SUM(player_games_pitching_innings_pitched) > 0
            THEN Round((9 * SUM(player_games_pitching_earned_runs_allowed)) / SUM(player_games_pitching_innings_pitched),2)
            ELSE NULL
    END AS ERA,

	Round(SUM(player_games_pitching_innings_pitched), 1) AS IP,
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

FROM
    player_games
INNER JOIN players ON players.players_playerID = player_games.player_games_playerID
where players.players_player_primary_position = '1'
GROUP BY
    players_playerID, players_player_last, players_player_first
order by players_player_last, players_player_first;

--Braves Record versus each team
WITH OpposingTeams AS (
    SELECT
        CASE
            WHEN gd.game_details_home_team = 1 THEN gd.game_details_visiting_team
            ELSE gd.game_details_home_team
        END AS opposing_team,
        game_details_winning_team,
        game_details_info_losing_team

    FROM game_details gd
    WHERE game_details_home_team = 1 OR game_details_visiting_team = 1
)
SELECT
    opposing_team as "Opponent Team ID",
	teams.teams_teammascot "Opponent Mascot",
    COUNT(*) AS Games_Played,
    SUM(CASE WHEN game_details_winning_team = 1 THEN 1 ELSE 0 END) AS Wins,
    SUM(CASE WHEN game_details_info_losing_team = 1 THEN 1 ELSE 0 END) AS Losses
FROM OpposingTeams
inner join teams on teams.teams_teamID = opposing_team
GROUP BY opposing_team, teams.teams_teammascot
ORDER BY opposing_team;
