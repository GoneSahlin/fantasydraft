"""draft
A fantasy football draft

Author: Zach Sahlin
"""

import pandas as pd
import os
from team import Team


class Draft:
    """A fantasy football draft"""

    def __init__(self, num_teams, pos_list=None):
        """
        Constructor

        :param num_teams: number of teams in the league
        """

        # default parameter
        if pos_list is None:
            pos_list = ['QB', 'RB', 'RB', 'WR', 'WR', 'TE', 'FLEX', 'ST', 'K']

        # declare variables
        self.player_df = pd.DataFrame()
        self.num_teams = num_teams
        self.teams = []
        self.next_team = 0
        self.direction = 0      # which way the picks are moving in the snake draft
        self.round = 0
        self.pos_list = pos_list

    def start(self):
        """Starts the draft"""

        self.read_players('espn_fantasy_projections.csv')
        self.create_teams(self.num_teams)
        self.calculate_draft_order(self.num_teams)

    def read_players(self, filename):
        """Reads in the player data from a csv file

        :param filename: name of the file with the player data
        """

        this_directory = os.path.dirname(__file__)
        self.player_df = pd.read_csv(os.path.join(this_directory, filename), index_col="RANK")
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

        self.teams = []
        for _ in range(num_teams):
            self.teams.append(Team(self, self.pos_list))
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

    def get_players(self, pos=None):
        """Gets the player list

        :returns player_df: DataFrame of all the players"""

        if pos is None:
            return self.player_df
        else:
            return self.player_df.groupby('Position').get_group(pos)

    def draft_player(self, player_rank, team):
        """Drafts a player to a team

        :param player_rank: the rank of the player to be drafted
        :param team: the team the player will be drafted to
        """

        selection = self.teams[team].make_selection()
        self.teams[team].add_player(1)

        self.player_df.at[player_rank, 'Picked'] = True
