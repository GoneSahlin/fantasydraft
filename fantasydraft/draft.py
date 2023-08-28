"""draft
A fantasy football draft

Author: Zach Sahlin
"""

import pandas as pd
import numpy as np

from team import Team
from simple_team import SimpleTeam
from user_team import UserTeam
from mcts_team import MCTSTeam
from player import Player
from utils import create_player_pos_dict, read_players


class Draft:
    """A fantasy football draft"""

    def __init__(self, num_teams, total_rounds=16, pos_list=None, flex_options=None, weights=None, players=None, player_pos_dict=None, round=0, cur_team_index=0, direction=0, teams=None):
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
        self.teams = teams

        # if teams is None:
        #     self.teams = self.create_teams(num_teams)
        # else:
        #     self.teams = teams

        if players is None:
            self.players = read_players()
        else:
            self.players = players

        # create free agent position lists
        if player_pos_dict is None:
            self.player_pos_dict = create_player_pos_dict(self.players)
        else:
            self.player_pos_dict = player_pos_dict
    
    def copy(self):
        new_players = self.players.copy()

        new_player_pos_dict = create_player_pos_dict(new_players)

        new_teams = [team.copy() for team in self.teams]

        new_draft = Draft(self.num_teams, self.total_rounds, pos_list=self.pos_list, flex_options=self.flex_options,
                          weights=self.weights, players=new_players, player_pos_dict=new_player_pos_dict, 
                          round=self.round, cur_team_index=self.cur_team_index, direction=self.direction, teams=new_teams)
        
        for team in new_teams:
            team.draft=new_draft
        
        return new_draft


    def get_players(self, pos=None):
        """Gets the player list

        :param pos: the position of the players to get, default None to return all players
        :returns player_df: DataFrame of all the players
        """
        if pos is None:
            return self.players
        
        if pos in self.player_pos_dict:
            return self.player_pos_dict[pos]
        else:
            print(f"Incorrect position: {pos}")
        

    def draft_player(self, player):
        """Drafts a player to a team

        :param team: the team the player will be drafted to
        """
        team = self.teams[self.cur_team_index]
        team.add_player(player)

        # remove player
        self.players.remove(player)
        self.get_players(player.position).remove(player)

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

    def is_draft_over(self):
        return self.round >= self.total_rounds

    def start(self):
        """Starts the draft
        """
        # drafts the players
        while not self.is_draft_over():
            cur_team = self.teams[self.cur_team_index]
            selection = cur_team.make_selection()

            self.draft_player(selection)  # draft player

            print(selection.name)

    def end(self):
        """Ends the draft and projects rankings
        """
        totals = []
        for team in self.teams:
            totals.append(team.calculate_total())
        print(totals)

        # for team in self.teams:
        #     print([player.points for player in team.roster])               

