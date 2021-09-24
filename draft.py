"""draft
A fantasy football draft

Author: Zach Sahlin
"""

import pandas as pd
import os
from team import Team


class Draft:
    """A fantasy football draft"""

    def __init__(self, num_teams):
        """
        Constructor

        :param num_teams: number of teams in the league
        """

        # declare vars
        self.player_df = pd.DataFrame()
        self.num_teams = num_teams
        self.teams = []
        self.next_team = 0
        self.direction = 0  # which way the picks are moving in the snake draft
        self.round = 0

    def start(self):
        """Starts the draft"""

        self.read_players("espn_fantasy_projections.txt")
        self.create_teams(self.num_teams)
        self.calculate_draft_order(self.num_teams)

    def read_players(self, filename):
        """Reads in the player data from a csv file

        :param filename: name of the file with the player data
        """

        this_directory = os.path.dirname(__file__)
        self.player_df = pd.read_csv(os.path.join(this_directory, filename))
        self.player_df["Picked"] = False

    def calculate_draft_order(self, num_teams):
        """Calculates the draft order based on the number of teams using a snake draft

        :param num_teams: number of teams in the league
        """
        pass

    def create_teams(self, num_teams):
        """Creates the teams in the draft

        :param num_teams: number of teams in the league
        """
        # num_teams = int(input("Number of teams: "))
        self.teams = []
        for _ in range(num_teams):
            self.teams.append(Team())
        print(self.teams)

    def next_turn(self, team):
        """Takes the next turn in the draft"""
        pass

    def get_next_team(self):
        """Gets the team with the next pick"""
        pass

    def end(self):
        """Ends the draft and projects rankings"""
        pass

    def get_players(self):
        """Gets the player list

        :returns player_df: DataFrame of all the players"""

        return self.player_df

    def get_players(self, pos):
        """Gets the players with position

        :param pos: the position of the players to get {'RB', 'WR', 'QB', 'TE', 'K', 'ST'}
        :returns player_pos_df: DataFrame for all the players with position pos
        """

        player_pos_df = self.player_df.groupby('Position').get_group(pos)

        return player_pos_df

    def draft_player(self, player_name, team):
        """Drafts a player to a team

        :param player_name: the name of the player to be drafted
        :param team: the team the player will be drafted to
        """
        pass
