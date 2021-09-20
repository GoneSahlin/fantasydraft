import pandas as pd

class Draft:
    # constructor
    def __init__(self):
        self.read_players("espn_fantasy_projections.txt")

    # read in the player data from csv
    def read_players(self, filename):
        self.players_df = pd.read_csv(filename)
        self.players_df["Picked"] = False

    # calculates draft order based on number of teams with a snake draft
    def calculate_draft_order(self):
        pass

    # initializes the teams
    def create_teams():
        num_teams = input("Number of teams: ")
        

    # starts the draft
    def start(self):
        pass

    # takes the next turn of the draft
    def next_turn(self):
        pass

    # gets the next teams turn
    def get_next_team(self):
        pass

    # ends the draft and projects rankings
    def end(self):
        pass

    # gets the player list
    def get_players(self):
        pass

    # gets the players with position pos
    def get_players(self, pos):
        pass

    # drafts a player
    def draft_player(self, player_name, team):
        pass
