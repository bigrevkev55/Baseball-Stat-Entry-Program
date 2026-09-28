#Author:  Kevin Thomas
#Date:    04-APR-2023
#Purpose: This program connects to my baseball projects database via data entry forms and stores the data there
#Version: 0.55
 
# Future Edits
#---------------------
# 1.  Move database to the same program dirctory and make this a .exe file that can be ran independant of VS Code - Consider migrating data to a SQLite3 DB
# 2.  Link the Player Creation form, and Game Creation form to the Player Game Entry Form so the user has one environment from wich to work
# 3.  Add in the logos of all the simulation games I play. Currently I only have logos for Strat O Matic, APBA, and Season Ticket.  
#     But I also play Payoff Pitch, Dynasty League, Downey Ultra Quick Baseball, and will play others in the future
# 4.  Change the top level logo - it's currently Strat's logo
# 5.  Create a form to enter the stats as the game is played instead of having to wait until after the game is played to enter all the stats for that game.
# 6.  Have a report menu or button so the user doesn't have to copy and paste SQL scripts in an external program to view stats and reports. 
# 7.  Add in error handling popups that make sense to the user and that can be seen in the program without relying on the command line.
# 8.  Make the confirmation message a pop up instead of a line in the command line
# 9.  Add Game Engine column to database (game_details table) and the Game Creation Entry Form
#10.  Add game play start time and game play finish time to Game Creation Entry form and connect it to the game_details table
#11.  Add blown saves to the forms and database
#12.  Fix the issue with sac bunts and sac flies (they count as ABs in the sql queries and aren't separated
#     as separate stats on the  forms/tables ...ie..they both go in as SAC)

import tkinter as Tk
from tkinter import *
from tkinter import PhotoImage
import pyodbc as odbc
from pyodbc import *
from PIL import ImageTk, Image

#Create Functions for the program
def save1():  
    #pull data from form into the function
    playerId=player_games_playerID_box.get()
    gameId=player_games_gameID_box.get()
    appearance=player_games_game_appearance_box.get()
    abs=player_games_ABs_box.get()
    hittingBB=player_games_hitting_walks_box.get()
    hittingHBP=player_games_hitting_HBP_box.get()
    hittingStrikeouts=player_games_hitting_strikeouts_box.get()
    runs=player_games_hitting_runs_box.get()
    hits=player_games_hitting_hits_box.get()
    doubles=player_games_hitting_doubles_box.get()
    triples=player_games_hitting_triples_box.get()
    hrs=player_games_hitting_homeruns_box.get()
    rbis=player_games_hitting_RBIs_box.get()
    sac=player_games_hitting_sacrificess_box.get()
    sb=player_games_hitting_SB_box.get()
    sba=player_games_hitting_SB_attempts_box.get()
    e=player_games_fielding_errors_box.get()
    ip=player_games_pitching_IP_box.get()
    w=player_games__win_box.get()
    l=player_games_loss_box.get()
    h=player_games_hold_box.get()
    s=player_games_save_box.get()
    ha=player_games_hits_allowed_box.get()
    bb=player_games_pitching_BBs_box.get()
    k=player_games_pitching_strikeouts_box.get()
    hbp=player_games_pitching_HBP_box.get()
    hra=player_games_pitching_homeruns_allowed_box.get()
    ra=player_games_pitching_runs_allowed_box.get()
    earnedRunsAllowed=player_games_pitching_earned_runs_allowed_box.get()
    cg=player_games_pitching_complete_game_box.get()
    so=player_games_pitching_shutout_box.get()
    wp=player_games_pitching_wild_pitch_box.get()
    bk=player_games_pitching_balk_box.get()


    # insert into table
    sql = 'INSERT INTO player_games(player_games_playerID,player_games_gameID,player_games_game_appearance,player_games_ABs,player_games_hitting_walks,player_games_hitting_HBP,player_games_hitting_strikeouts,player_games_hitting_runs,player_games_hitting_hits,player_games_hitting_doubles,player_games_hitting_triples,player_games_hitting_homeruns,player_games_hitting_RBIs,player_games_hitting_sacrificess,player_games_hitting_SB,player_games_hitting_SB_attempts,player_games_fielding_errors, player_games_pitching_innings_pitched, player_games__win, player_games_loss, player_games_hold,player_games_save, player_games_hits_allowed, player_games_pitching_BBs,player_games_pitching_strikeouts, player_games_pitching_HBP, player_games_pitching_homeruns_allowed, player_games_pitching_runs_allowed, player_games_pitching_earned_runs_allowed, player_games_pitching_complete_game,player_games_pitching_shutout,player_games_pitching_wild_pitch, player_games_pitching_balk)  Values (?, ?, ?, ?, ?, ?, ?,?,?,?,?, ?, ?, ?, ?, ?, ?,?,?,?,?, ?, ?, ?, ?, ?, ?,?,?,?,?,?,?)'

    val = playerId, gameId, appearance, abs, hittingBB, hittingHBP, hittingStrikeouts, runs, hits, doubles, triples, hrs,rbis,sac,sb,sba,e,ip, w, l, h,s,ha, bb, k, hbp, hra, ra, earnedRunsAllowed, cg, so, wp, bk

    # Create a Database or Connect to one
    conn = odbc.connect('Driver={SQL Server};'
                        'Server=DESKTOP-SCL1250\SQLEXPRESS01;'
                        'Database=stratBB;'
                        'Trusted_Connection=yes;')
    c = conn.cursor()

    c.execute(sql, val)

    # Commit Changes
    c.commit()
    # Close Connection
    c.close()

     #Clear the text boxes
    player_games_playerID_box.delete(0,END)
    #player_games_gameID_box.delete(0,END)
    #player_games_game_appearance_box.delete(0,END)
    player_games_ABs_box.delete(0,END)
    player_games_hitting_walks_box.delete(0,END)
    player_games_hitting_HBP_box.delete(0,END)
    player_games_hitting_strikeouts_box.delete(0,END)
    player_games_hitting_runs_box.delete(0,END)
    player_games_hitting_hits_box.delete(0,END)
    player_games_hitting_doubles_box.delete(0,END)
    player_games_hitting_triples_box.delete(0,END)
    player_games_hitting_homeruns_box.delete(0,END)
    player_games_hitting_RBIs_box.delete(0,END)
    player_games_hitting_sacrificess_box.delete(0,END)
    player_games_hitting_SB_box.delete(0,END)
    player_games_hitting_SB_attempts_box.delete(0,END)
    player_games_fielding_errors_box.delete(0,END)
    player_games_pitching_IP_box.delete(0,END)
    player_games__win_box.delete(0,END)
    player_games_loss_box.delete(0,END)
    player_games_hold_box.delete(0,END)
    player_games_save_box.delete(0,END)
    player_games_hits_allowed_box.delete(0,END)
    player_games_pitching_BBs_box.delete(0,END)
    player_games_pitching_strikeouts_box.delete(0,END)
    player_games_pitching_HBP_box.delete(0,END)
    player_games_pitching_homeruns_allowed_box.delete(0,END)
    player_games_pitching_runs_allowed_box.delete(0,END)
    player_games_pitching_earned_runs_allowed_box.delete(0,END)
    player_games_pitching_complete_game_box.delete(0,END)
    player_games_pitching_shutout_box.delete(0,END)
    player_games_pitching_wild_pitch_box.delete(0,END)
    player_games_pitching_balk_box.delete(0,END)
    player_games_playerID_box.focus()

    print('Stats have been entered and saved for player ' +playerId + ' you may now enter the next player\'s stats')

def exit1():
      root.destroy()

def clear1():
    player_games_playerID_box.delete(0,END)
    player_games_gameID_box.delete(0,END)
    player_games_game_appearance_box.delete(0,END)
    player_games_ABs_box.delete(0,END)
    player_games_hitting_walks_box.delete(0,END)
    player_games_hitting_HBP_box.delete(0,END)
    player_games_hitting_strikeouts_box.delete(0,END)
    player_games_hitting_runs_box.delete(0,END)
    player_games_hitting_hits_box.delete(0,END)
    player_games_hitting_doubles_box.delete(0,END)
    player_games_hitting_triples_box.delete(0,END)
    player_games_hitting_homeruns_box.delete(0,END)
    player_games_hitting_RBIs_box.delete(0,END)
    player_games_hitting_sacrificess_box.delete(0,END)
    player_games_hitting_SB_box.delete(0,END)
    player_games_hitting_SB_attempts_box.delete(0,END)
    player_games_fielding_errors_box.delete(0,END)
    player_games_pitching_IP_box.delete(0,END)
    player_games__win_box.delete(0,END)
    player_games_loss_box.delete(0,END)
    player_games_hold_box.delete(0,END)
    player_games_save_box.delete(0,END)
    player_games_hits_allowed_box.delete(0,END)
    player_games_pitching_BBs_box.delete(0,END)
    player_games_pitching_strikeouts_box.delete(0,END)
    player_games_pitching_HBP_box.delete(0,END)
    player_games_pitching_homeruns_allowed_box.delete(0,END)
    player_games_pitching_runs_allowed_box.delete(0,END)
    player_games_pitching_earned_runs_allowed_box.delete(0,END)
    player_games_pitching_complete_game_box.delete(0,END)
    player_games_pitching_shutout_box.delete(0,END)
    player_games_pitching_wild_pitch_box.delete(0,END)
    player_games_pitching_balk_box.delete(0,END)
    player_games_playerID_box.focus()

#Functions to click <ENTER> on button
def save(event):  
  save1()

def exit(event):
  exit1()

def clear(even):
      clear1()

##Create Tkinter Window for data entry form
root = Tk()
root.title("Player Game Entry Form")

#Create image object for icon and contral panel
img=ImageTk.PhotoImage(Image.open("Strat O Matic Logo.png"))
ApbaImg=ImageTk.PhotoImage(Image.open("APBA Logo.png"))
seasonTicketImg=ImageTk.PhotoImage(Image.open("Season Ticket Logo.png"))

icon=PhotoImage=img
root.iconphoto(True, icon) #True sets this icon as the default icon for future top level windows 

#Create Panels
mainPanel=PanedWindow(root, orient="horizontal", bd=4,background='red', relief='sunken')
mainPanel.grid(column=0, columnspan=25,row=0,rowspan=60)
left_panel=PanedWindow(bd=4, orient="vertical", background='blue',relief="raised")
center_panel=PanedWindow(bd=4, orient='vertical', background='blue', relief='raised')
right_panel=PanedWindow(bd=4,orient="vertical", background='blue', relief='raised')

mainPanel.add(left_panel)
mainPanel.add(center_panel)
mainPanel.add(right_panel)

#Create Frames
#--Hitting Frame
HittingFrame=LabelFrame(left_panel, background='bisque', text="Hitting Stats", width=100)
HittingFrame.pack_propagate=True
HittingFrame.grid(row=1, column=1, columnspan=2,pady=15, padx=15)
left_panel.add(HittingFrame)

#--Pitching Frame
pitchingFrame = LabelFrame(center_panel,background='bisque', text="Pitching Stats", padx=20, pady=20)
pitchingFrame.pack_propagate=True
pitchingFrame.grid(column=50, columnspan=5, row=1)
center_panel.add(pitchingFrame)

#--Control Frame
controlFrame = LabelFrame(right_panel, background='bisque', text="Controls", padx=20, pady=20)
controlFrame.pack_propagate=True
controlFrame.grid(column=1, columnspan=4, row=5)
right_panel.add(controlFrame)

#Put images object in control frame
picLabel=Label(controlFrame,image=img)
picLabel.pack()

picText=Label(controlFrame, text="Strat-O-Matic Baseball", bg='bisque', pady=5, font='Helvetica')
picText.pack()

apbaPicLabel=Label(controlFrame,image=ApbaImg, pady=5)
apbaPicLabel.pack()

apbaPicText=Label(controlFrame, text="APBA Baseball", bg='bisque', pady=5, font='Helvetica')
apbaPicText.pack()

seasonTicketPicLabel=Label(controlFrame, image=seasonTicketImg, pady=5)
seasonTicketPicLabel.pack()

seasonTicketPicText=Label(controlFrame, text="Season Ticket Baseball", bg='bisque', pady=5, font='Helvetica')
seasonTicketPicText.pack()


#Create Database Connection
conn = odbc.connect('Driver={SQL Server};'
                    'Server=DESKTOP-SCL1250\SQLEXPRESS01;'
                    'Database=stratBB;'
                    'Trusted_Connection=yes;')
# Create Cursor
c = conn.cursor()

#Hitting Entry Box Labels 
player_games_playerID_box_label = Label(HittingFrame, text="*PlayerID", bg='bisque')
player_games_playerID_box_label.grid(row=0, column=1, sticky='w')

player_games_gameID_box_label = Label(HittingFrame, text="*GameID", bg='bisque')
player_games_gameID_box_label.grid(row=1, column=1, sticky='w')

player_games_game_appearance_box_label = Label(HittingFrame, text="Game Played", bg='bisque')
player_games_game_appearance_box_label.grid(row=2, column=1, sticky='w')

player_games_hitting_hits_box_label = Label(HittingFrame, text="Hits", bg='bisque')
player_games_hitting_hits_box_label.grid(row=3, column=1, sticky='w')

player_games_ABs_box_label = Label(HittingFrame, text= "ABs", bg='bisque')
player_games_ABs_box_label.grid(row=4, column = 1, sticky='w')

player_games_hitting_walks_box = Label(HittingFrame, text="BBs", bg='bisque')
player_games_hitting_walks_box.grid(row=5, column = 1, sticky='w')

player_games_hitting_HBP_box_label = Label(HittingFrame, text="HBP", bg='bisque')
player_games_hitting_HBP_box_label.grid(row=6, column=1, sticky='w')

player_games_hitting_strikeouts_box_label = Label(HittingFrame, text="K", bg='bisque')
player_games_hitting_strikeouts_box_label.grid(row=7, column=1, sticky='w')

player_games_hitting_runs_box_label = Label(HittingFrame, text="Runs", bg='bisque')
player_games_hitting_runs_box_label.grid(row=8, column=1, sticky='w')

player_games_hitting_doubles_box_label = Label(HittingFrame, text="2B", bg='bisque')
player_games_hitting_doubles_box_label.grid(row=9, column=1, sticky='w')

player_games_hitting_triples_box_label = Label(HittingFrame, text="3B", bg='bisque')
player_games_hitting_triples_box_label.grid(row=10, column=1, sticky='w')

player_games_hitting_homeruns_box_label = Label(HittingFrame, text="HR", bg='bisque')
player_games_hitting_homeruns_box_label.grid(row=11, column=1, sticky='w')

player_games_hitting_RBIs_box_label = Label(HittingFrame, text="RBIs", bg='bisque')
player_games_hitting_RBIs_box_label.grid(row=12, column=1, sticky='w')

player_games_hitting_sacrificess_box_label = Label(HittingFrame, text="SAC", bg='bisque')
player_games_hitting_sacrificess_box_label.grid(row=13, column=1, sticky='w')

player_games_hitting_SB_box_label = Label(HittingFrame, text="SB", bg='bisque')
player_games_hitting_SB_box_label.grid(row=14, column=1, sticky='w')

player_games_hitting_SB_attempts_box_label = Label(HittingFrame, text="SBA", bg='bisque')
player_games_hitting_SB_attempts_box_label.grid(row=15, column=1, sticky='w')

player_games_fielding_errors_box_label = Label(HittingFrame, text="E", bg='bisque')
player_games_fielding_errors_box_label.grid(row=16, column=1, sticky='w')

#Pitching Entry Box Labels
player_games_pitching_IP_box_label = Label(pitchingFrame, text="IP", bg='bisque')
player_games_pitching_IP_box_label.grid(row=1, column=1, sticky='w')

player_games__win_box_label = Label(pitchingFrame, text="W", bg='bisque')
player_games__win_box_label.grid(row=2, column=1, sticky='w')

player_games_loss_box_label = Label(pitchingFrame, text="L", bg='bisque')
player_games_loss_box_label.grid(row=3, column=1, sticky='w')

player_games_hold_box_label = Label(pitchingFrame, text="Hold", bg='bisque')
player_games_hold_box_label.grid(row=4, column=1, sticky='w')

player_games_save_box_label = Label(pitchingFrame, text="S", bg='bisque')
player_games_save_box_label.grid(row=5, column=1, sticky='w')

player_games_hits_allowed_box_label = Label(pitchingFrame, text="Hits Allowed", bg='bisque')
player_games_hits_allowed_box_label.grid(row=6, column=1, sticky='w')

player_games_pitching_BBs_box_label = Label(pitchingFrame, text="BB", bg='bisque')
player_games_pitching_BBs_box_label.grid(row=7, column=1, sticky='w')

player_games_pitching_strikeouts_box_label = Label(pitchingFrame, text="K", bg='bisque')
player_games_pitching_strikeouts_box_label.grid(row=8, column=1, sticky='w')

player_games_pitching_HBP_box_label = Label(pitchingFrame, text="HBP", bg='bisque')
player_games_pitching_HBP_box_label.grid(row=9, column=1, sticky='w')

player_games_pitching_homeruns_allowed_box_label = Label(pitchingFrame, text="HRA", bg='bisque')
player_games_pitching_homeruns_allowed_box_label.grid(row=10, column=1, sticky='w')

player_games_pitching_runs_allowed_box_label = Label(pitchingFrame, text="RA", bg='bisque')
player_games_pitching_runs_allowed_box_label.grid(row=11, column=1, sticky='w')

player_games_pitching_earned_runs_allowed_box_label = Label(pitchingFrame, text="Earned Runs Allowed", bg='bisque')
player_games_pitching_earned_runs_allowed_box_label.grid(row=12, column=1, sticky='w')

player_games_pitching_complete_game_box_label = Label(pitchingFrame, text="CG", bg='bisque')
player_games_pitching_complete_game_box_label.grid(row=13, column=1, sticky='w')

player_games_pitching_shutout_box_label = Label(pitchingFrame, text="Shutout", bg='bisque')
player_games_pitching_shutout_box_label.grid(row=14, column=1, sticky='w')

player_games_pitching_wild_pitch_box_label = Label(pitchingFrame, text="WP", bg='bisque')
player_games_pitching_wild_pitch_box_label.grid(row=15, column=1, sticky='w')

player_games_pitching_balk_box_label = Label(pitchingFrame, text="BK", bg='bisque')
player_games_pitching_balk_box_label.grid(row=16, column=1, sticky='w')

#Hitting Data Entry Boxes
player_games_playerID_box = Entry(HittingFrame, width=25)
player_games_playerID_box.grid(row=0, column=2)

player_games_gameID_box = Entry(HittingFrame, width=25)
player_games_gameID_box.grid(row=1, column=2)

player_games_game_appearance_box = Entry(HittingFrame, width=25)
player_games_game_appearance_box.grid(row=2, column=2)

player_games_hitting_hits_box = Entry(HittingFrame, width=25)
player_games_hitting_hits_box.grid(row=3, column=2)

player_games_ABs_box = Entry(HittingFrame, width=25)
player_games_ABs_box.grid(row=4, column = 2)

player_games_hitting_walks_box = Entry(HittingFrame, width=25)
player_games_hitting_walks_box.grid(row=5, column = 2)

player_games_hitting_HBP_box = Entry(HittingFrame, width=25)
player_games_hitting_HBP_box.grid(row=6, column=2)

player_games_hitting_strikeouts_box = Entry(HittingFrame, width=25)
player_games_hitting_strikeouts_box.grid(row=7, column=2)

player_games_hitting_runs_box = Entry(HittingFrame, width=25)
player_games_hitting_runs_box.grid(row=8, column=2)

player_games_hitting_doubles_box = Entry(HittingFrame, width=25)
player_games_hitting_doubles_box.grid(row=9, column=2)

player_games_hitting_triples_box = Entry(HittingFrame, width=25)
player_games_hitting_triples_box.grid(row=10, column=2)

player_games_hitting_homeruns_box = Entry(HittingFrame, width=25)
player_games_hitting_homeruns_box.grid(row=11, column=2)

player_games_hitting_RBIs_box = Entry(HittingFrame, width=25)
player_games_hitting_RBIs_box.grid(row=12, column=2)

player_games_hitting_sacrificess_box = Entry(HittingFrame, width=25)
player_games_hitting_sacrificess_box.grid(row=13, column=2)

player_games_hitting_SB_box = Entry(HittingFrame, width=25)
player_games_hitting_SB_box.grid(row=14, column=2)

player_games_hitting_SB_attempts_box = Entry(HittingFrame, width=25)
player_games_hitting_SB_attempts_box.grid(row=15, column=2)

player_games_fielding_errors_box = Entry(HittingFrame, width=25)
player_games_fielding_errors_box.grid(row=16, column=2)

#Pitching Data Entry Boxes
player_games_pitching_IP_box = Entry(pitchingFrame, width=25)
player_games_pitching_IP_box.grid(row=1, column=2)

player_games__win_box = Entry(pitchingFrame, width=25)
player_games__win_box.grid(row=2, column=2)

player_games_loss_box = Entry(pitchingFrame, width=25)
player_games_loss_box.grid(row=3, column=2)

player_games_hold_box = Entry(pitchingFrame, width=25)
player_games_hold_box.grid(row=4, column=2)

player_games_save_box = Entry(pitchingFrame, width=25)
player_games_save_box.grid(row=5, column=2)

player_games_hits_allowed_box = Entry(pitchingFrame, width=25)
player_games_hits_allowed_box.grid(row=6, column=2)

player_games_pitching_BBs_box = Entry(pitchingFrame, width=25)
player_games_pitching_BBs_box.grid(row=7, column=2)

player_games_pitching_strikeouts_box = Entry(pitchingFrame, width=25)
player_games_pitching_strikeouts_box.grid(row=8, column=2)

player_games_pitching_HBP_box = Entry(pitchingFrame, width=25)
player_games_pitching_HBP_box.grid(row=9, column=2)

player_games_pitching_homeruns_allowed_box = Entry(pitchingFrame, width=25)
player_games_pitching_homeruns_allowed_box.grid(row=10, column=2)

player_games_pitching_runs_allowed_box = Entry(pitchingFrame, width=25)
player_games_pitching_runs_allowed_box.grid(row=11, column=2)

player_games_pitching_earned_runs_allowed_box = Entry(pitchingFrame, width=25)
player_games_pitching_earned_runs_allowed_box.grid(row=12, column=2)

player_games_pitching_complete_game_box = Entry(pitchingFrame, width=25)
player_games_pitching_complete_game_box.grid(row=13, column=2)

player_games_pitching_shutout_box = Entry(pitchingFrame, width=25)
player_games_pitching_shutout_box.grid(row=14, column=2)

player_games_pitching_wild_pitch_box = Entry(pitchingFrame, width=25)
player_games_pitching_wild_pitch_box.grid(row=15, column=2)

player_games_pitching_balk_box = Entry(pitchingFrame, width=25)
player_games_pitching_balk_box.grid(row=16, column=2)

# Create Buttons in the control frame
#--Clear Button
clear_btn = Button(controlFrame, text="Clear Entries", command=clear1, pady=10)
clear_btn.bind("<Return>", clear)
clear_btn.pack(pady=5, fill='x')

#--Save Button
save_btn = Button(controlFrame, text='Save Record', command=save1, pady=10)
save_btn.bind("<Return>", save)
save_btn.pack(pady=5, fill='x')

#--Edit Button

#--Search Button

#--Close Button
close_btn = Button(controlFrame, text='Exit', command=exit1, bg='green', fg='white', pady=10)
close_btn.bind("<Return>", exit)
close_btn.pack(pady=5, fill = 'x')

# Create an Edit Button an put it in the control frame

root.mainloop()
