"""draft
A fantasy football draft

Author: Zach Sahlin
"""

import pandas as pd
from copy import deepcopy

from team import Team
from simple_team import SimpleTeam
from user_team import UserTeam
from player import Player


class Draft:
    """A fantasy football draft"""

    def __init__(self, num_teams, total_rounds=16, pos_list=None, flex_options=None, weights=None, player_filename="data/players.csv", players=None, player_position_dict=None, round=0, cur_team_index=0, direction=0, teams=None):
        """
        Constructor

        :param num_teams: number of teams in the league
        """

        # default parameter
        if pos_list is None:
            pos_list = ['QB', 'RB', 'RB', 'WR', 'WR', 'TE', 'FLEX', 'ST', 'K']

        if flex_options is None:
            flex_options = ["RB", "WR", "TE"]

        if weights is None:
            weights = {'QB': [60, 40],
                       'RB': [70, 70, 40, 20],
                       'WR': [70, 70, 40, 20],
                       'TE': [60, 40],
                       'FLEX': [60, 40],
                       'ST': [60, 30, 10],
                       'K': [50, 20, 20, 10]}

        # declare variables
        self.num_teams = num_teams
        self.cur_team_index = cur_team_index
        self.direction = direction      # which way the picks are moving in the snake draft, 0 is forwards, 1 is backwards
        self.round = round
        self.total_rounds = total_rounds
        self.pos_list = pos_list
        self.flex_options = flex_options
        self.weights = weights

        if teams is None:
            self.teams = self.create_teams(num_teams)
        else:
            self.teams = teams

        if players is None:
            self.players = self.read_players(player_filename)
        else:
            self.players = players

        # create free agent position lists
        if player_position_dict is None:
            self.player_postition_dict = {"QB": [], "RB": [], "WR": [], "TE": [], "ST": [], "K": []}
        
            for player in self.players:
                if player.position in self.player_postition_dict:
                    self.player_postition_dict[player.position].append(player)
                else:
                    print(f"Incorrect position {player.position} for Player: {player.name}")
        else:
            self.player_postition_dict = player_position_dict

    
    def copy(self):
        new_players = self.players.copy()
        new_player_position_dict = deepcopy(self.player_postition_dict)
        new_teams = self.teams.


        new_draft = Draft(self.num_teams, self.total_rounds, pos_list=self.pos_list, flex_options=self.flex_options,
                          weights=self.weights, players=new_players, player_position_dict=new_player_position_dict, 
                          round=self.round, cur_team_index=self.cur_team_index, direction=self.direction, teams=new_teams)
        
        
        
        return new_draft
        

    def read_players(self, filename):
        """Reads in the player data from a csv file

        :param filename: name of the file with the player data
        """
        player_df = pd.read_csv(filename)

        players = []
        for _, row in player_df.iterrows():
            players.append(Player(row['name'], row['position'], row['points'], row['rank']))

        return players

        
    def create_teams(self, num_teams):
        """Creates the teams in the draft

        :param num_teams: number of teams in the league
        """
        teams = []
        for _ in range(num_teams):
            teams.append(SimpleTeam(self))

        return teams

    def get_players(self, pos=None):
        """Gets the player list

        :param pos: the position of the players to get, default None to return all players
        :returns player_df: DataFrame of all the players
        """
        if pos is None:
            return self.players
        
        if pos in self.player_postition_dict:
            return self.player_position_dict[pos]
        else:
            print(f"Incorrect position: {pos}")
        

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
        while self.round < self.total_rounds:
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

        # for team in self.teams:
        #     print([player.points for player in team.roster])
