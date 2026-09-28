import tkinter as Tk
from tkinter import *
from PIL import ImageTk, Image
from database import get_connection   # <-- NEW: SQLite connection


class PlayerCreationForm:
    def __init__(self):
        self.root = Tk()
        self.root.title("Strat BB Player Creation Form")

        # -----------------------------
        # Panels
        # -----------------------------
        mainPanel = PanedWindow(self.root, orient="vertical", bd=4, background='red', relief='sunken')
        mainPanel.pack(fill="both", expand=True)

        topPanel = PanedWindow(mainPanel, bd=4, orient="horizontal", background='blue', relief="raised")
        center_panel = PanedWindow(mainPanel, bd=4, orient='horizontal', background='blue', relief='raised')
        bottomPanel = PanedWindow(mainPanel, bd=4, orient="horizontal", background='blue', relief='raised')

        mainPanel.add(topPanel)
        mainPanel.add(center_panel)
        mainPanel.add(bottomPanel)


        # -----------------------------
        # Frames
        # -----------------------------
        keyBlockFrame = LabelFrame(topPanel, text="Key Block", width=100)
        keyBlockFrame.pack_propagate(True)
        keyBlockFrame.grid(row=1, column=1, columnspan=2, pady=15, padx=15)
        topPanel.add(keyBlockFrame)

        playerFrame = LabelFrame(center_panel, text="Player Information", padx=20, pady=20)
        playerFrame.pack_propagate(True)
        playerFrame.grid(column=50, columnspan=5, row=1)
        center_panel.add(playerFrame)

        controlFrame = LabelFrame(bottomPanel, text="Controls", padx=20, pady=20)
        controlFrame.pack_propagate(True)
        controlFrame.grid(column=1, columnspan=4, row=5)
        bottomPanel.add(controlFrame)

        # -----------------------------
        # Key Block
        # -----------------------------
        playerId = Label(keyBlockFrame, text="Use this form to create new players. Player IDs will be auto created")
        playerId.grid(row=1, column=1, sticky="w")

        try:
            img = ImageTk.PhotoImage(Image.open("Strat O Matic Logo.png"))
            picLabel = Label(keyBlockFrame, image=img)
            picLabel.image = img
            picLabel.grid(row=1, column=2)
        except:
            pass  # If image missing, don't crash

        # -----------------------------
        # Labels
        # -----------------------------
        Label(playerFrame, text="Player Season").grid(row=1, column=1, sticky='w')
        Label(playerFrame, text="Last Name").grid(row=2, column=1, sticky='w')
        Label(playerFrame, text="First Name").grid(row=3, column=1, sticky='w')
        Label(playerFrame, text="Primary Position").grid(row=4, column=1, sticky='w')
        Label(playerFrame, text="Team ID").grid(row=5, column=1, sticky='w')
        Label(playerFrame, text="Team Season").grid(row=6, column=1, sticky='w')

        # -----------------------------
        # Entry Boxes
        # -----------------------------
        self.playerSeasonBox = Entry(playerFrame, width=25)
        self.lastNameBox = Entry(playerFrame, width=25)
        self.firstNameBox = Entry(playerFrame, width=25)
        self.positionBox = Entry(playerFrame, width=25)
        self.teamIdBox = Entry(playerFrame, width=25)
        self.teamSeasonBox = Entry(playerFrame, width=25)

        self.playerSeasonBox.grid(row=1, column=2)
        self.lastNameBox.grid(row=2, column=2)
        self.firstNameBox.grid(row=3, column=2)
        self.positionBox.grid(row=4, column=2)
        self.teamIdBox.grid(row=5, column=2)
        self.teamSeasonBox.grid(row=6, column=2)

        # -----------------------------
        # Save Button
        # -----------------------------
        save_btn = Button(controlFrame, text='Save Record', command=self.save_record)
        save_btn.pack()

        self.root.mainloop()

    # -----------------------------
    # Save Function (SQLite)
    # -----------------------------
    def save_record(self):
        playerSeason = self.playerSeasonBox.get()
        lastName = self.lastNameBox.get()
        firstName = self.firstNameBox.get()
        position = self.positionBox.get()
        team = self.teamIdBox.get()
        teamSeason = self.teamSeasonBox.get()

        sql = """
            INSERT INTO players (
                players_player_season,
                players_player_last,
                players_player_first,
                players_player_primary_position,
                players_player_teamID,
                players_player_team_season
            ) VALUES (?, ?, ?, ?, ?, ?)
        """

        values = (playerSeason, lastName, firstName, position, team, teamSeason)

        conn = get_connection()
        c = conn.cursor()
        c.execute(sql, values)
        conn.commit()
        conn.close()

        # Clear fields
        self.playerSeasonBox.delete(0, END)
        self.lastNameBox.delete(0, END)
        self.firstNameBox.delete(0, END)
        self.positionBox.delete(0, END)
        self.teamIdBox.delete(0, END)
        self.teamSeasonBox.delete(0, END)

        print(f"{firstName} {lastName} has been created and saved.")
