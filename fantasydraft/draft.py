"""draft
A fantasy football draft

Author: Zach Sahlin
"""

import pandas as pd
import os

from team import Team
from simple_team import SimpleTeam
from user_team import UserTeam
from player import Player


class Draft:
    """A fantasy football draft"""

    def __init__(self, num_teams, pos_list=None, flex_options=None):
        """
        Constructor

        :param num_teams: number of teams in the league
        """

        # default parameter
        if pos_list is None:
            pos_list = ['QB', 'RB', 'RB', 'WR', 'WR', 'TE', 'FLEX', 'ST', 'K']

        if flex_options is None:
            flex_options = ["RB", "WR", "FLEX"]

        # declare variables
        self.num_teams = num_teams
        self.cur_team_index = 0
        self.direction = 0      # which way the picks are moving in the snake draft, 0 is forwards, 1 is backwards
        self.round = 0
        self.pos_list = pos_list
        self.flex_options = flex_options

        self.teams = self.create_teams(num_teams)
        self.players = self.read_players(os.path.join("data", "espn_fantasy_projections.csv"))

        # create free agent position lists
        self.qbs = []
        self.rbs = []
        self.wrs = []
        self.tes = []
        self.sts = []
        self.ks = []
        for player in self.players:
            match player.position:
                case 'QB':
                    self.qbs.append(player)
                    continue
                case 'RB':
                    self.rbs.append(player)
                    continue
                case 'WR':
                    self.wrs.append(player)
                    continue
                case 'TE':
                    self.tes.append(player)
                    continue
                case 'ST':
                    self.sts.append(player)
                    continue
                case 'K':
                    self.ks.append(player)
                    continue
                case _:
                    print(f"Incorrect position {player.position} for Player: {player.name}")
        

    def read_players(self, filename):
        """Reads in the player data from a csv file

        :param filename: name of the file with the player data
        """
        # this_directory = os.path.dirname(__file__)
        player_df = pd.read_csv(filename, index_col="RANK")

        players = []
        for index, row in player_df.iterrows():
            players.append(Player(row['PLAYER'], row['Position'], row['Total pts'], index))

        return players

        
    def create_teams(self, num_teams):
        """Creates the teams in the draft

        :param num_teams: number of teams in the league
        """
        teams = []
        for _ in range(num_teams):
            teams.append(SimpleTeam(self, self.pos_list))

        return teams

    def get_players(self, pos=None):
        """Gets the player list

        :param pos: the position of the players to get, default None to return all players
        :returns player_df: DataFrame of all the players
        """
    
        match pos:
            case None:
                return self.players
            case 'QB':
                return self.qbs
            case 'RB':
                return self.rbs
            case 'WR':
                return self.wrs
            case 'TE':
                return self.tes
            case 'ST':
                return self.sts
            case 'K':
                return self.ks
            case _:
                print("Incorrect position")

    def draft_player(self, team: Team):
        """Drafts a player to a team

        :param team: the team the player will be drafted to
        """
        selection = team.make_selection()
        team.add_player(selection)

        # remove player
        self.players.remove(selection)
        self.get_players(selection.position).remove(selection)

    def start(self):
        """Starts the draft
        """
        # drafts the players
        while self.round < len(self.pos_list):
            self.draft_player(self.teams[self.cur_team_index])  # draft player

            if self.direction == 0:
                if self.cur_team_index < self.num_teams - 1:
                    self.cur_team_index += 1
                else:
                    self.direction = 1
                    self.round += 1
            else:
                if self.cur_team_index > 0:
                    self.cur_team_index -= 1
                else:
                    self.direction = 0
                    self.round += 1

    def end(self):
        """Ends the draft and projects rankings
        """
        totals = []
        for team in self.teams:
            totals.append(team.calculate_total())
        print(totals)
