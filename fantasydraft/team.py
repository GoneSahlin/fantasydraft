"""team
A fantasy football team

Author: Zach Sahlin
"""

from abc import ABC, abstractmethod

from player import Player


class Team(ABC):
    """A fantasy football team
    """
    def __init__(self, draft, pos_list):
        """Constructor"""

        self.draft = draft
        self.roster = []
        self.empty_positions = pos_list.copy()
        self.postiion_counts = {"QB": 0, "RB": 0, "WR": 0, "TE": 0, "ST": 0, "K": 0}

    def add_player(self, player: Player):
        """adds a player to the team

        :param player_rank: the rank of the player to add
        """
        self.roster.append(player)

        if player.position in self.empty_positions:
            self.empty_positions.remove(player.position)
        elif player.position in self.draft.flex_options and "FLEX" in self.empty_positions:
            self.empty_positions.remove("FLEX")

        self.postiion_counts[player.position] += 1

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
        """Calculates the total projected points

        :returns total_points: the total projected points for all starting players
        """
        positions_available = self.draft.pos_list.copy()
        total_points = 0
        for player in sorted(self.roster, key=lambda player: player.points):
            if player.position in positions_available:
                positions_available.remove(player.position)
                total_points += player.points
            elif player.position in self.draft.flex_options and "FLEX" in positions_available:
                positions_available.remove("FLEX")
                total_points += player.points

        return total_points
