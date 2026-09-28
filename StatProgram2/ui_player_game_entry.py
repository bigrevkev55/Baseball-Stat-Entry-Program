import tkinter as Tk
from tkinter import *
from PIL import ImageTk, Image
from database import get_connection
import os


class PlayerGameEntryForm:
    def __init__(self):
        self.root = Tk()
        self.root.title("Player Game Entry Form")

        # -----------------------------
        # Main container frame
        # -----------------------------
        main_frame = Frame(self.root, bg="gray90")
        main_frame.pack(fill="both", expand=True, padx=10, pady=10)

        # Left = Hitting/Fielding, Center = Pitching, Right = Controls/Logos
        self.hitting_frame = LabelFrame(main_frame, text="Hitting & Fielding", bg="bisque", padx=10, pady=10)
        self.hitting_frame.grid(row=0, column=0, sticky="nsew", padx=(0, 10))

        self.pitching_frame = LabelFrame(main_frame, text="Pitching", bg="bisque", padx=10, pady=10)
        self.pitching_frame.grid(row=0, column=1, sticky="nsew", padx=(0, 10))

        self.control_frame = LabelFrame(main_frame, text="Controls", bg="bisque", padx=10, pady=10)
        self.control_frame.grid(row=0, column=2, sticky="nsew")

        # Make columns expand nicely
        main_frame.columnconfigure(0, weight=3)
        main_frame.columnconfigure(1, weight=3)
        main_frame.columnconfigure(2, weight=2)
        main_frame.rowconfigure(0, weight=1)

        # -----------------------------
        # Build UI sections
        # -----------------------------
        self._load_logos()
        self._build_hitting_fields()
        self._build_pitching_fields()
        self._build_control_buttons()


        # -----------------------------
        # Start the window
        # -----------------------------
        self.root.mainloop()

    # ---------------------------------------------------------
    # Load logos (compact, clean, resized, safe)
    # ---------------------------------------------------------
    def _load_logos(self):
        try:
            max_size = (160, 70)

            # --- Strat-O-Matic ---
            strat_raw = Image.open("Strat O Matic Logo.png").convert("RGBA")
            bg = Image.new("RGBA", strat_raw.size, (255, 255, 255, 255))
            bg.paste(strat_raw, mask=strat_raw)
            strat_raw = bg
            strat_raw.thumbnail(max_size, Image.LANCZOS)
            self.strat_img = ImageTk.PhotoImage(strat_raw)

            # --- APBA ---
            apba_raw = Image.open("APBA Logo.png").convert("RGBA")
            bg = Image.new("RGBA", apba_raw.size, (255, 255, 255, 255))
            bg.paste(apba_raw, mask=apba_raw)
            apba_raw = bg
            apba_raw.thumbnail(max_size, Image.LANCZOS)
            self.apba_img = ImageTk.PhotoImage(apba_raw)

            # --- Season Ticket ---
            st_raw = Image.open("Season Ticket Logo.png").convert("RGBA")
            bg = Image.new("RGBA", st_raw.size, (255, 255, 255, 255))
            bg.paste(st_raw, mask=st_raw)
            st_raw = bg
            st_raw.thumbnail(max_size, Image.LANCZOS)
            self.st_img = ImageTk.PhotoImage(st_raw)

            # Place them
            Label(self.control_frame, image=self.strat_img, bg="bisque").pack(pady=(0, 5))
            Label(self.control_frame, text="Strat-O-Matic Baseball", bg="bisque").pack(pady=(0, 10))

            Label(self.control_frame, image=self.apba_img, bg="bisque").pack(pady=(0, 5))
            Label(self.control_frame, text="APBA Baseball", bg="bisque").pack(pady=(0, 10))

            Label(self.control_frame, image=self.st_img, bg="bisque").pack(pady=(0, 5))
            Label(self.control_frame, text="Season Ticket Baseball", bg="bisque").pack(pady=(0, 10))

        except Exception as e:
            Label(self.control_frame, text="Simulation Logos", bg="bisque", font=("Arial", 12, "bold")).pack(pady=10)
            Label(self.control_frame, text=f"(Logo load error: {e})", bg="bisque", wraplength=180).pack(pady=5)

    # ---------------------------------------------------------
    # Hitting & Fielding Fields
    # ---------------------------------------------------------
    def _build_hitting_fields(self):
        r = 0

        def add_field(label_text):
            nonlocal r
            lbl = Label(self.hitting_frame, text=label_text, bg="bisque", anchor="w")
            lbl.grid(row=r, column=0, sticky="w", pady=2)

            entry = Entry(self.hitting_frame, width=20)
            entry.grid(row=r, column=1, pady=2, padx=(5, 0))

            r += 1
            return entry

        self.playerID = add_field("*Player ID")
        self.gameID = add_field("*Game ID")
        self.appearance = add_field("Game Played (Y/N)")
        self.hits = add_field("Hits")
        self.abs = add_field("ABs")
        self.walks = add_field("BBs")
        self.hbp = add_field("HBP")
        self.strikeouts = add_field("K")
        self.runs = add_field("Runs")
        self.doubles = add_field("2B")
        self.triples = add_field("3B")
        self.homeruns = add_field("HR")
        self.rbis = add_field("RBIs")
        self.sac = add_field("SAC")
        self.sb = add_field("SB")
        self.sba = add_field("SBA")
        self.errors = add_field("Errors (E)")

    # ---------------------------------------------------------
    # Pitching Fields
    # ---------------------------------------------------------
    def _build_pitching_fields(self):
        r = 0

        def add_field(label_text):
            nonlocal r
            lbl = Label(self.pitching_frame, text=label_text, bg="bisque", anchor="w")
            lbl.grid(row=r, column=0, sticky="w", pady=2)

            entry = Entry(self.pitching_frame, width=20)
            entry.grid(row=r, column=1, pady=2, padx=(5, 0))

            r += 1
            return entry

        self.ip = add_field("IP")
        self.win = add_field("W")
        self.loss = add_field("L")
        self.hold = add_field("Hold")
        self.save = add_field("Save")
        self.hits_allowed = add_field("Hits Allowed")
        self.pitching_bb = add_field("BB")
        self.pitching_k = add_field("K")
        self.pitching_hbp = add_field("HBP")
        self.hra = add_field("HRA")
        self.ra = add_field("RA")
        self.earned_runs = add_field("Earned Runs Allowed")
        self.complete_game = add_field("CG")
        self.shutout = add_field("Shutout")
        self.wild_pitch = add_field("WP")
        self.balk = add_field("BK")

    def _build_control_buttons(self):
        """Create Save, Clear, and Exit buttons in the control panel."""

        # Save Button
        save_btn = Button(
            self.control_frame,
            text="Save Record",
            width=18,
            pady=5,
            command=self._save_record
        )
        save_btn.pack(pady=(20, 5))

        # Clear Button
        clear_btn = Button(
            self.control_frame,
            text="Clear Fields",
            width=18,
            pady=5,
            command=self._clear_fields
        )
        clear_btn.pack(pady=5)

        # Exit Button
        exit_btn = Button(
            self.control_frame,
            text="Exit",
            width=18,
            pady=5,
            bg="green",
            fg="white",
            command=self.root.destroy
        )
        exit_btn.pack(pady=20)


    def _save_record(self):
            """Save the player game record to SQLite."""

            # Required fields
            player_id = self.playerID.get().strip()
            game_id = self.gameID.get().strip()

            if not player_id or not game_id:
                print("Player ID and Game ID are required.")
                return

            # Collect all fields
            data = {
                "player_games_playerID": player_id,
                "player_games_gameID": game_id,
                "player_games_game_appearance": self.appearance.get().strip(),
                "player_games_ABs": self.abs.get().strip(),
                "player_games_hitting_walks": self.walks.get().strip(),
                "player_games_hitting_HBP": self.hbp.get().strip(),
                "player_games_hitting_strikeouts": self.strikeouts.get().strip(),
                "player_games_hitting_runs": self.runs.get().strip(),
                "player_games_hitting_hits": self.hits.get().strip(),
                "player_games_hitting_doubles": self.doubles.get().strip(),
                "player_games_hitting_triples": self.triples.get().strip(),
                "player_games_hitting_homeruns": self.homeruns.get().strip(),
                "player_games_hitting_RBIs": self.rbis.get().strip(),
                "player_games_hitting_sacrificess": self.sac.get().strip(),
                "player_games_hitting_SB": self.sb.get().strip(),
                "player_games_hitting_SB_attempts": self.sba.get().strip(),
                "player_games_fielding_errors": self.errors.get().strip(),
                "player_games__win": self.win.get().strip(),
                "player_games_loss": self.loss.get().strip(),
                "player_games_hold": self.hold.get().strip(),
                "player_games_save": self.save.get().strip(),
                "player_games_hits_allowed": self.hits_allowed.get().strip(),
                "player_games_pitching_BBs": self.pitching_bb.get().strip(),
                "player_games_pitching_strikeouts": self.pitching_k.get().strip(),
                "player_games_pitching_HBP": self.pitching_hbp.get().strip(),
                "player_games_pitching_homeruns_allowed": self.hra.get().strip(),
                "player_games_pitching_runs_allowed": self.ra.get().strip(),
                "player_games_pitching_earned_runs_allowed": self.earned_runs.get().strip(),
                "player_games_pitching_complete_game": self.complete_game.get().strip(),
                "player_games_pitching_shutout": self.shutout.get().strip(),
                "player_games_pitching_wild_pitch": self.wild_pitch.get().strip(),
                "player_games_pitching_balk": self.balk.get().strip(),
                "player_games_pitching_innings_pitched": self.ip.get().strip()
            }



            # Convert empty strings to None
            clean_data = {}
            for k, v in data.items():
                if v == "":
                    clean_data[k] = None
                else:
                    clean_data[k] = v

            try:
                conn = get_connection()
                cursor = conn.cursor()

                placeholders = ", ".join(["?"] * len(clean_data))
                columns = ", ".join(clean_data.keys())

                sql = "INSERT INTO player_games (" + columns + ") VALUES (" + placeholders + ")"
                cursor.execute(sql, list(clean_data.values()))

                conn.commit()
                conn.close()

                print("Record saved successfully.")

                # Clear fields and refocus
                self._clear_fields()

            except Exception as e:
                print("Error saving record:", e)


    def _clear_fields(self):
        """Clear all entry fields."""
        # Hitting fields
        for field in [
            self.playerID, self.gameID, self.appearance, self.hits, self.abs,
            self.walks, self.hbp, self.strikeouts, self.runs, self.doubles,
            self.triples, self.homeruns, self.rbis, self.sac, self.sb,
            self.sba, self.errors
       ]:
            field.delete(0, END)

        # Pitching fields
        for field in [
            self.ip, self.win, self.loss, self.hold, self.save,
            self.hits_allowed, self.pitching_bb, self.pitching_k,
            self.pitching_hbp, self.hra, self.ra, self.earned_runs,
            self.complete_game, self.shutout, self.wild_pitch, self.balk
        ]:
            field.delete(0, END)

        self.playerID.focus()


# Standalone test
if __name__ == "__main__":
    PlayerGameEntryForm()
