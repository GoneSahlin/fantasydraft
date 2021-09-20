from team import Team
import pandas as pd

class Draft:
    # constructor
    def __init__(self, num_teams):
        self.read_players("espn_fantasy_projections.txt")
        self.create_teams(num_teams)
        self.calculate_draft_order(num_teams)

    # read in the player data from csv
    def read_players(self, filename):
        self.players_df = pd.read_csv(filename)
        self.players_df["Picked"] = False

    # calculates draft order based on number of teams with a snake draft
    def calculate_draft_order(self, num_teams):
        pass

    # initializes the teams
    def create_teams(self, num_teams):
        # num_teams = int(input("Number of teams: "))
        self.teams = []
        for i in range(num_teams):
            self.teams.append(Team())

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
