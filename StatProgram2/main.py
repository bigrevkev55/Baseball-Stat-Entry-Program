"""
Author: Kevin Thomas
Original Date: 04-APR-2023
Current Revision: February 7, 2026
Version: 0.55

Purpose:
    Originally created to connect to my baseball projects database through
    data entry forms (Player Creation, Game Creation, and Player Game
    Entry) and store project data. This updated version now initializes the
    modern system by creating the portable SQLite database (stratbb.db),
    building all core tables, installing reporting views, and providing the
    get_connection() function used by those same forms and all future modules.

    This file now serves as the main application launcher for the StratBB system.
    It provides a simple main menu that opens the Player Creation form and will
    later open Game Creation, Player Game Entry, Reports, and Live Scoring modules.
    
# Future Edits
#---------------------
# 1.  Move database to the same program dirctory and make this a .exe file that can be ran independant of VS Code - Consider migrating data to a SQLite3 DB - Done February 2026
# 2.  Link the Player Creation form, and Game Creation form to the Player Game Entry Form so the user has one environment from wich to work - Done February 2026
# 3.  Add in the logos of all the simulation games I play. Currently I only have logos for Strat O Matic, APBA, and Season Ticket.  
#     But I also play Payoff Pitch, Dynasty League, Downey Ultra Quick Baseball, and will play others in the future
# 4.  Change the top level logo - it's currently Strat's logo
# 5.  Create a form to enter the stats as the game is played instead of having to wait until after the game is played to enter all the stats for that game.
# 6.  Have a report menu or button so the user doesn't have to copy and paste SQL scripts in an external program to view stats and reports. - Several views created in February 2026 but a more robust #     #      system is still needed
# 7.  Add in error handling popups that make sense to the user and that can be seen in the program without relying on the command line.
# 8.  Make the confirmation message a pop up instead of a line in the command line
# 9.  Add Game Engine column to database (game_details table) and the Game Creation Entry Form
#10.  Add game play start time and game play finish time to Game Creation Entry form and connect it to the game_details table
#11.  Add blown saves to the forms and database
#12.  Fix the issue with sac bunts and sac flies (they count as ABs in the sql queries and aren't separated
#     as separate stats on the  forms/tables ...ie..they both go in as SAC)
#13.  Add winning pitcher, losing Pitcher, and saving pitcher to game results
#14.  Add team scores to game details table and data entry forms
#15.  Have the system check for a database on opening from main.py and creating an empty database if not exists.


"""

import tkinter as Tk
from tkinter import *
from ui_player_creation import PlayerCreationForm   # Import your forms
from ui_game_creation import GameCreationForm
from ui_player_game_entry import PlayerGameEntryForm



class StratBBMainMenu:
    def __init__(self):
        self.root = Tk()
        self.root.title("StratBB Main Menu")
        self.root.geometry("400x300")

        # Title
        title = Label(self.root, text="StratBB Application", font=("Arial", 18, "bold"))
        title.pack(pady=20)

        # Player Creation Button
        btn_player_creation = Button(
            self.root,
            text="Player Creation Form",
            width=25,
            command=self.open_player_creation
        )
        btn_player_creation.pack(pady=10)

        # Game Creation Button
        btn_game_creation = Button(
            self.root,
            text="Game Creation Form",
            width=25,
            command=self.open_game_creation
        )
        btn_game_creation.pack(pady=10)

        #Player Game Entry Button
        btn_stats_entry_creation = Button(
            self.root,
            text="Enter Player Game Stats",
            width=25,
            command=self.open_player_game_entry
        )
        btn_stats_entry_creation.pack(pady=10)


        # Future buttons will go here:
        # - Reports
        # - Live Scoring

        # Exit Button
        quit_btn = Button(self.root, text="Exit Program", width=25, command=self.root.quit)
        quit_btn.pack(pady=20)

        self.root.mainloop()

    def open_player_creation(self):
        PlayerCreationForm()   

    def open_game_creation(self):
        GameCreationForm()

    def open_player_game_entry(self):
        PlayerGameEntryForm()



# Run the main menu
if __name__ == "__main__":
    StratBBMainMenu()
