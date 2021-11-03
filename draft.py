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
        self.cur_team = 0
        self.direction = 0      # which way the picks are moving in the snake draft, 0 is forwards, 1 is backwards
        self.round = 0
        self.pos_list = pos_list

    def read_players(self, filename):
        """Reads in the player data from a csv file

        :param filename: name of the file with the player data
        """
        this_directory = os.path.dirname(__file__)
        self.player_df = pd.read_csv(os.path.join(this_directory, filename), index_col="RANK")
        self.player_df["Picked"] = False

    def create_teams(self, num_teams):
        """Creates the teams in the draft

        :param num_teams: number of teams in the league
        """
        self.teams = []
        for i in range(num_teams):
            self.teams.append(Team(self, self.pos_list, i))

    def get_players(self, pos=None):
        """Gets the player list

        :param pos: the position of the players to get, default None to return all players
        :returns player_df: DataFrame of all the players
        """
        if pos is None:
            return self.player_df
        else:
            return self.player_df.groupby('Position').get_group(pos)

    def draft_player(self, team):
        """Drafts a player to a team

        :param team: the team the player will be drafted to
        """
        selection = self.teams[team].make_selection()
        self.teams[team].add_player(selection)

        self.player_df.at[selection, 'Picked'] = True

    def start(self):
        """Starts the draft
        """
        self.read_players('espn_fantasy_projections.csv')   # read in players
        self.create_teams(self.num_teams)                   # create teams

        # drafts the players
        while self.round < len(self.pos_list):
            self.draft_player(self.cur_team)    # draft player

            if self.direction == 0:
                if self.cur_team < self.num_teams - 1:
                    self.cur_team += 1
                else:
                    self.direction = 1
                    self.round += 1
            else:
                if self.cur_team > 0:
                    self.cur_team -= 1
                else:
                    self.direction = 0
                    self.round += 1

    def end(self):
        """Ends the draft and projects rankings
        """
        totals = []
        for team in self.teams:
            totals.append(team.calculate_total())
            print(team.my_players_df)
        print(totals)

