import tkinter as Tk
from tkinter import *
from database import get_connection


class GameCreationForm:
    def __init__(self):
        self.root = Tk()
        self.root.title("Strat BB Game Details Form")

        # -----------------------------
        # Main PanedWindow
        # -----------------------------
        mainPanel = PanedWindow(self.root, orient="horizontal", bd=4, background='red', relief='sunken')
        mainPanel.pack(fill="both", expand=True)

        left_panel = PanedWindow(mainPanel, bd=4, orient="vertical", background='blue', relief="raised")
        center_panel = PanedWindow(mainPanel, bd=4, orient='vertical', background='blue', relief='raised')
        right_panel = PanedWindow(mainPanel, bd=4, orient="vertical", background='blue', relief='raised')

        mainPanel.add(left_panel)
        mainPanel.add(center_panel)
        mainPanel.add(right_panel)

        # -----------------------------
        # Frames
        # -----------------------------
        gameInfoFrame = LabelFrame(left_panel, background='bisque', text="Game Information", width=100)
        gameInfoFrame.pack_propagate(True)
        gameInfoFrame.grid(row=1, column=1, columnspan=2, pady=15, padx=15)
        left_panel.add(gameInfoFrame)

        controlFrame = LabelFrame(center_panel, background='bisque', text="Controls", padx=20, pady=20)
        controlFrame.pack_propagate(True)
        controlFrame.grid(column=1, columnspan=4, row=5)
        center_panel.add(controlFrame)

        infoFrame = LabelFrame(right_panel, background='bisque', text="Information", padx=20, pady=20)
        infoFrame.pack_propagate(True)
        infoFrame.grid(column=50, columnspan=5, row=1)
        right_panel.add(infoFrame)

        # -----------------------------
        # Entry Boxes
        # -----------------------------
        self.project_abbrevation_box = Entry(gameInfoFrame, width=25)
        self.project_abbrevation_box.grid(row=2, column=3)

        self.visiting_team_box = Entry(gameInfoFrame, width=25)
        self.visiting_team_box.grid(row=3, column=3)

        self.home_team_box = Entry(gameInfoFrame, width=25)
        self.home_team_box.grid(row=4, column=3)

        self.winning_team_box = Entry(gameInfoFrame, width=25)
        self.winning_team_box.grid(row=5, column=3)

        self.losing_team_box = Entry(gameInfoFrame, width=25)
        self.losing_team_box.grid(row=6, column=3)

        self.start_time_box = Entry(gameInfoFrame, width=25)
        self.start_time_box.grid(row=7, column=3)

        self.end_time_box = Entry(gameInfoFrame, width=25)
        self.end_time_box.grid(row=8, column=3)

        # -----------------------------
        # Labels
        # -----------------------------
        game_id_label = Label(gameInfoFrame, text="*GameID")
        game_id_label.grid(row=1, column=2)

        self.auto_game_id_label = Label(gameInfoFrame, text="Auto")
        self.auto_game_id_label.grid(row=1, column=3)

        project_abbrevation_label = Label(gameInfoFrame, text="*Project Code")
        project_abbrevation_label.grid(row=2, column=2)

        visiting_team = Label(gameInfoFrame, text="*Visiting Team")
        visiting_team.grid(row=3, column=2)

        home_team_label = Label(gameInfoFrame, text="*Home Team")
        home_team_label.grid(row=4, column=2)

        winning_team_label = Label(gameInfoFrame, text="*Winning Team")
        winning_team_label.grid(row=5, column=2)

        losing_team_label = Label(gameInfoFrame, text="*Losing Team")
        losing_team_label.grid(row=6, column=2)

        start_time_label = Label(gameInfoFrame, text='Start Time (hh:mm)')
        start_time_label.grid(row=7, column=2)

        end_time_label = Label(gameInfoFrame, text='End Time (hh:mm)')
        end_time_label.grid(row=8, column=2)

        infolabel1 = Label(infoFrame, text="This project uses Strat-O-Matic Baseball")
        infolabel1.grid(row=1, column=1, sticky='w')

        infolabel2 = Label(infoFrame, text='Items with * are required')
        infolabel2.grid(row=2, column=1, sticky='w', pady=10)

        # -----------------------------
        # Save Button
        # -----------------------------
        save_btn = Button(controlFrame, text='Save Record', command=self.save_record)
        save_btn.pack()

        self.root.mainloop()

    # -----------------------------
    # Helper: Get Max Game ID
    # -----------------------------
    def get_max_game_id(self):
        sql = "SELECT MAX(game_details_gameid) FROM game_details;"
        conn = get_connection()
        c = conn.cursor()
        c.execute(sql)
        row = c.fetchone()
        conn.close()
        return row[0] if row and row[0] is not None else None

    # -----------------------------
    # Save Function (SQLite)
    # -----------------------------
    def save_record(self):
        pa = self.project_abbrevation_box.get()
        vt = self.visiting_team_box.get()
        ht = self.home_team_box.get()
        wt = self.winning_team_box.get()
        lt = self.losing_team_box.get()
        st = self.start_time_box.get()
        et = self.end_time_box.get()

        sql = """
            INSERT INTO game_details (
                game_details_projectID,
                game_details_visiting_team,
                game_details_home_team,
                game_details_winning_team,
                game_details_info_losing_team,
                game_details_start_time,
                game_details_end_time
            ) VALUES (?, ?, ?, ?, ?, ?, ?)
        """

        values = (pa, vt, ht, wt, lt, st, et)

        conn = get_connection()
        c = conn.cursor()
        c.execute(sql, values)
        conn.commit()
        conn.close()

        # Get new game ID
        new_game_id = self.get_max_game_id()
        if new_game_id is not None:
            self.auto_game_id_label.config(text=str(new_game_id))

        # Clear fields (except project code if you want to keep it)
        # self.project_abbrevation_box.delete(0, END)
        self.visiting_team_box.delete(0, END)
        self.home_team_box.delete(0, END)
        self.winning_team_box.delete(0, END)
        self.losing_team_box.delete(0, END)
        self.start_time_box.delete(0, END)
        self.end_time_box.delete(0, END)

        self.visiting_team_box.focus()

        print(f"Game {new_game_id} has been created and saved...you may now create the next game.")

