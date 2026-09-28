import tkinter as Tk
from tkinter import *
import pyodbc as odbc
from pyodbc import *
from PIL import ImageTk, Image

def save1():
    #pull data from form into the function
    playerSeason=playerSeasonBox.get()
    lastName=lastNameBox.get()
    firstName=firstNameBox.get()
    position=positionBox.get()
    team=teamIdBox.get()
    teamSeason=teamSeasonBox.get()

    #insert data into the table
    sql='INSERT INTO players(players_player_season, players_player_last, players_player_first, players_player_primary_position, players_player_teamID, players_player_team_season) VALUES (?,?,?,?,?,?)'
    val= playerSeason, lastName, firstName, position, team, teamSeason

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
    playerSeasonBox.delete(0,END)
    lastNameBox.delete(0,END)
    firstNameBox.delete(0,END)
    positionBox.delete(0,END)
    teamIdBox.delete(0,END)
    teamSeasonBox.delete(0,END)

    print(f'{firstName} {lastName} has been created and saved...you may now create another player')

##Function to click <ENTER> on button and save
def save(event):
    save1()


root = Tk()
root.title("Strat BB Player Creation Form")
#root.iconbitmap(default='Strat O Matic Logo.ico')


#Create Panels
mainPanel=PanedWindow(root, orient="vertical", bd=4,background='red', relief='sunken')
mainPanel.grid(column=0, columnspan=25,row=0,rowspan=60)
topPanel=PanedWindow(bd=4, orient="horizontal", background='blue',relief="raised")
center_panel=PanedWindow(bd=4, orient='horizontal', background='blue', relief='raised')
bottomPanel=PanedWindow(bd=4,orient="horizontal", background='blue', relief='raised')

mainPanel.add(topPanel)
mainPanel.add(center_panel)
mainPanel.add(bottomPanel)


#Create Frames
keyBlockFrame=LabelFrame(topPanel, text="Key Block", width=100)
keyBlockFrame.pack_propagate=True
keyBlockFrame.grid(row=1, column=1, columnspan=2,pady=15, padx=15)
topPanel.add(keyBlockFrame)

playerFrame = LabelFrame(center_panel, text="Player Information", padx=20, pady=20)
playerFrame.pack_propagate=True
playerFrame.grid(column=50, columnspan=5, row=1)
center_panel.add(playerFrame)

controlFrame = LabelFrame(bottomPanel, text="Controls", padx=20, pady=20)
controlFrame.pack_propagate=True
controlFrame.grid(column=1, columnspan=4, row=5)
bottomPanel.add(controlFrame)

#Create Database Connection
conn = odbc.connect('Driver={SQL Server};'
                    'Server=DESKTOP-SCL1250\SQLEXPRESS01;'
                    'Database=stratBB;'
                    'Trusted_Connection=yes;')
# Create Cursor
c = conn.cursor()

#Key Block Information
playerId = Label(keyBlockFrame, text = "Use this form to create new players.  Player IDs will be auto created")
playerId.grid(row=1, column=1, sticky="w")

img=ImageTk.PhotoImage(Image.open("Strat O Matic Logo.png"), size=1)

picLabel=Label(keyBlockFrame,image=img)
picLabel.grid(row=1, column=2)

#Player Info Box Labels 
playerSeasonLabel = Label(playerFrame, text="Player Season")
playerSeasonLabel.grid(row=1, column=1, sticky='w')

lastNameLabel = Label(playerFrame, text= "Last Name")
lastNameLabel.grid(row=2, column=1, sticky="w")

firstNameLabel = Label(playerFrame, text = "First Name")
firstNameLabel.grid(row=3, column=1, sticky='w')

positionLabel = Label(playerFrame, text="Primary Position")
positionLabel.grid(row=4, column = 1, sticky='w')

teamIdLabel = Label(playerFrame, text="Team ID")
teamIdLabel.grid(row=5, column = 1, sticky='w')

teamSeasonLabel = Label(playerFrame, text="Team Season")
teamSeasonLabel.grid(row=6, column = 1, sticky='w')


#Player Info Entry Boxes
playerSeasonBox = Entry(playerFrame, width=25)
playerSeasonBox.grid(row=1, column=2)

lastNameBox = Entry(playerFrame, width=25)
lastNameBox.grid(row=2, column=2)

firstNameBox = Entry(playerFrame, width=25)
firstNameBox.grid(row=3, column=2)

positionBox = Entry(playerFrame, width=25)
positionBox.grid(row=4, column=2)

teamIdBox = Entry(playerFrame, width=25)
teamIdBox.grid(row=5, column=2)

teamSeasonBox = Entry(playerFrame, width=25)
teamSeasonBox.grid(row=6, column=2)

#Controls Frame
# Create an Save Button
save_btn = Button(controlFrame, text='Save Record', command=save1)
save_btn.bind("<Return>", save)
save_btn.pack()


root.mainloop()