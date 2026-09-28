
import tkinter as Tk
from tkinter import *
import pyodbc as odbc
from pyodbc import *

#Create Function to get game ID
def getMaxGameId():
    sql='SELECT max(game_details_gameid) from game_details;'
    
     # Create a Database or Connect to one
    conn = odbc.connect('Driver={SQL Server};'
                        'Server=DESKTOP-SCL1250\SQLEXPRESS01;'
                        'Database=stratBB;'
                        'Trusted_Connection=yes;')
    c = conn.cursor()
    c.execute(sql)
    maxId = c.fetchall()
    return maxId

# Create Save Functions
##Function to click button and save
def save1():  
    #pull data from form into the program
    pa=project_abbrevation_box.get()
    vt=visiting_team_box.get()
    ht=home_team_box.get()
    wt=winning_team_box.get()
    lt=losing_team_box.get()
    st=start_time_box.get()
    et=end_time_box.get()
    
    # insert into table
    sql = 'INSERT INTO game_details(game_details_projectID,game_details_visiting_team,game_details_home_team,game_details_winning_team,game_details_info_losing_team, game_details_start_time, game_details_end_time) Values (?, ?, ?, ?, ?, ?, ?)' 

    val =  pa, vt, ht, wt, lt,st,et

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
    project_abbrevation_box.delete(0,END)
    visiting_team_box.delete(0,END)
    home_team_box.delete(0,END)
    winning_team_box.delete(0,END)
    losing_team_box.delete(0,END)
    start_time_box.delete(0,END)
    end_time_box.delete(0,END)

    newGameId = getMaxGameId()

    print(f'Game {newGameId} has been created and saved...you may now create the next game.')

##Function to click <ENTER> on button and save
def save(event):  
    #pull data from form into the program
    pa=project_abbrevation_box.get()
    vt=visiting_team_box.get()
    ht=home_team_box.get()
    wt=winning_team_box.get()
    lt=losing_team_box.get()
    st=start_time_box.get()
    et=end_time_box.get()
    
    # insert into table
    sql = 'INSERT INTO game_details(game_details_projectID,game_details_visiting_team,game_details_home_team,game_details_winning_team,game_details_info_losing_team, game_details_start_time, game_details_end_time) Values (?, ?, ?, ?, ?, ?, ?)' 

    val =  pa, vt, ht, wt, lt, st, et

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
    #project_abbrevation_box.delete(0,END)
    #visiting_team_box.delete(0,END)
    #home_team_box.delete(0,END)
    winning_team_box.delete(0,END)
    losing_team_box.delete(0,END)
    start_time_box.delete(0,END)
    end_time_box.delete(0,END)
    visiting_team_box.focus()

    print('Data has been entered and saved...you may now enter the next game\'s data')


root = Tk()
root.title("Strat BB Game Details Form")
#root.iconbitmap('C:/Users/bigre/OneDrive/Stratbb.ico')

#Create Panels
mainPanel=PanedWindow(root, orient="horizontal", bd=4,background='red', relief='sunken')
mainPanel.grid(column=0, columnspan=25,row=0,rowspan=60)
left_panel=PanedWindow(bd=4, orient="vertical", background='blue',relief="raised")
center_panel=PanedWindow(bd=4, orient='vertical', background='blue', relief='raised')
right_panel=PanedWindow(bd=4,orient="vertical", background='blue', relief='raised')

mainPanel.add(left_panel)
mainPanel.add(center_panel)
mainPanel.add(right_panel)

##Create Frames
gameInfoFrame=LabelFrame(left_panel, background='bisque', text="Game Information", width=100)
gameInfoFrame.pack_propagate=True
gameInfoFrame.grid(row=1, column=1, columnspan=2,pady=15, padx=15)
left_panel.add(gameInfoFrame)

#gameStatsFrame=LabelFrame(left_panel, text="Game Stats", background='bisque',foreground='blue', padx=20, pady=10, width=100)
#gameStatsFrame.pack_propagate=True
#gameStatsFrame.grid(row=6, column=2, pady=15, padx=15)
#left_panel.add(gameStatsFrame)

#resultFrame=LabelFrame(left_panel,background='bisque', text="Results", padx=15, pady=15, width=100)
#resultFrame.pack_propagate=True
#resultFrame.grid(row=36,column=3, columnspan=2, pady=15,padx=15)
#left_panel.add(resultFrame)

controlFrame = LabelFrame(center_panel, background='bisque', text="Controls", padx=20, pady=20)
controlFrame.pack_propagate=True
controlFrame.grid(column=1, columnspan=4, row=5)
center_panel.add(controlFrame)

infoFrame = LabelFrame(right_panel,background='bisque', text="Information", padx=20, pady=20)
infoFrame.pack_propagate=True
infoFrame.grid(column=50, columnspan=5, row=1)
right_panel.add(infoFrame)

#Create Database Connection
conn = odbc.connect('Driver={SQL Server};'
                    'Server=DESKTOP-SCL1250\SQLEXPRESS01;'
                    'Database=stratBB;'
                    'Trusted_Connection=yes;')
# Create Cursor
c = conn.cursor()

#Game Info Data Entry Boxes
project_abbrevation_box = Entry(gameInfoFrame, width=25)
project_abbrevation_box.grid(row=2, column=3)

visiting_team_box = Entry(gameInfoFrame, width=25)
visiting_team_box.grid(row=3, column=3)

home_team_box = Entry(gameInfoFrame, width=25)
home_team_box.grid(row=4, column=3)

winning_team_box = Entry(gameInfoFrame, width=25)
winning_team_box.grid(row=5, column=3)

losing_team_box = Entry(gameInfoFrame, width=25)
losing_team_box.grid(row=6, column=3)

start_time_box = Entry(gameInfoFrame, width=25)
start_time_box.grid(row=7, column=3)

end_time_box = Entry(gameInfoFrame, width=25)
end_time_box.grid(row=8, column=3)



# Create Text Box Labels
game_id_label = Label(gameInfoFrame, text="*GameID")
game_id_label.grid(row=1, column=2)

auto_game_id_label = Label(gameInfoFrame, text = "Auto")
auto_game_id_label.grid(row=1, column=3)

project_abbrevation_label = Label(gameInfoFrame,text="*Project Code")
project_abbrevation_label.grid(row=2, column=2)

visiting_team = Label(gameInfoFrame, text="*Visiting Team")
visiting_team.grid(row=3, column=2)

home_team_label = Label(gameInfoFrame, text="*Home Team")
home_team_label.grid(row=4, column=2)

winning_team_label = Label(gameInfoFrame,text="*Winning Team")
winning_team_label.grid(row=5, column=2) 

losing_team_label = Label(gameInfoFrame,text="*Losing Team")
losing_team_label.grid(row=6, column=2) 

start_time_label = Label(gameInfoFrame, text='Start Time (hh:mm)')
start_time_label.grid(row=7, column=2)

end_time_label = Label(gameInfoFrame, text='End Time (hh:mm)')
end_time_label.grid(row=8, column=2)

infolabel1 = Label(infoFrame, text="This project uses Strat-O-Matic Baseball")
#infolabel1.pack_propagate()
infolabel1.grid(row=1, column=1, sticky='w')

infolabel2 = Label(infoFrame, text='Items with * are required')
#infolabel2.pack_propagate()
infolabel2.grid(row=2, column=1, sticky='w', pady=10)


# Create an Save Button
save_btn = Button(controlFrame, text='Save Record', command=save1)
save_btn.bind("<Return>", save)
save_btn.pack()
#save_btn.grid(row=46, column=3, columnspan=1, pady=10, padx=10, ipadx=132)
#right_panel.add(save_btn)


root.mainloop()

