"""team
A fantasy football team

Author: Zach Sahlin
"""

from abc import ABC, abstractmethod
from copy import deepcopy
import numpy as np

from player import Player


class Team(ABC):
    """A fantasy football team
    """
    def __init__(self, draft, roster=None, empty_positions=None, position_counts=None):
        """Constructor"""

        self.draft = draft

        if roster is None:
            self.roster = []
        else:
            self.roster = roster

        if empty_positions is None:
            self.empty_positions = draft.pos_list.copy()
        else:
            self.empty_positions = empty_positions

        if position_counts is None:
            self.position_counts = {"QB": 0, "RB": 0, "WR": 0, "TE": 0, "ST": 0, "K": 0}
        else:
            self.position_counts = position_counts

    def copy(self):
        new_roster = self.roster.copy()
        new_empty_positions = self.empty_positions.copy()
        new_position_counts = self.position_counts.copy()
        
        new_team = Team(self.draft, roster=new_roster, empty_positions=new_empty_positions, position_counts=new_position_counts)

        return new_team

    def add_player(self, player: Player):
        """adds a player to the team

        :param player_rank: the rank of the player to add
        """
        self.roster.append(player)

        if player.position in self.empty_positions:
            self.empty_positions.remove(player.position)
        elif player.position in self.draft.flex_options and "FLEX" in self.empty_positions:
            self.empty_positions.remove("FLEX")

        self.position_counts[player.position] += 1

    def get_empty_positions(self):
        """Gets the positions that haven't been filled yet

        :returns empty_positions: the positions on the team that are empty
        """
        return self.empty_positions

    @abstractmethod
    def make_selection(self) -> Player:
        """Makes the next pick

        simple algorithm to select pick

        :return:
        """
        pass

    def calculate_total(self) -> int:
        """Calculates the total projected points based off of the weights

        :returns total_points: the total projected points for all starting players
        """

        weights_left = deepcopy(self.draft.weights)

        total_points = 0
        for player in self.roster:
            # move to highest weight available for position
            pos_weights = weights_left[player.position]
            if pos_weights:
                pos_weight = pos_weights[0]
            else:
                pos_weight = 0

            flex_weight = 0
            if player.position in self.draft.flex_options:
                flex_weights = weights_left["FLEX"]
                if flex_weights:
                    flex_weight = flex_weights[0]

            if not flex_weight or pos_weight >= flex_weight:
                weight = pos_weight
                if pos_weight:
                    pos_weights.pop(0)
            else:
                weight = flex_weight
                if flex_weight:
                    flex_weights.pop(0)

            total_points += player.points * weight / 100

        # for remaining weights use the mean of the top 3 free agents
        for pos in weights_left:
            for weight in weights_left[pos]:
                if pos == 'FLEX':
                    flex_player_points = []
                    for flex_pos in self.draft.flex_options:
                        flex_player_points.extend([player.points for player in self.draft.get_players(flex_pos)[:3]])
                    mean_points = np.mean(sorted(flex_player_points)[:3])
                else:
                    mean_points = np.mean([player.points for player in self.draft.get_players(pos)[:3]])
                
                total_points += mean_points * weight / 100

        return total_points

        # positions_available = self.draft.pos_list.copy()
        # total_points = 0
        # for player in sorted(self.roster, key=lambda player: player.points):
        #     if player.position in positions_available:
        #         positions_available.remove(player.position)
        #         total_points += player.points
        #     elif player.position in self.draft.flex_options and "FLEX" in positions_available:
        #         positions_available.remove("FLEX")
        #         total_points += player.points

        # return total_points
