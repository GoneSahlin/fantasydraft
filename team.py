"""team
A fantasy football team

Author: Zach Sahlin
"""

import pandas as pd


class Team:
    """A fantasy football team"""

    def __init__(self, draft, pos_list):
        """Constructor"""

        self.draft = draft
        self.my_players = []
        self.empty_positions = pos_list

    def add_player(self, player_rank):
        """adds a player to the team

        :param player_rank: the rank of the player to add
        """

        self.my_players.append(player_rank)
        player_pos = self.draft.get_player_df().loc[player_rank]['Position']
        self.empty_positions.remove(player_pos)

    def get_empty_positions(self):
        """Gets the positions that haven't been filled yet

        :returns empty_positions: the positions on the team that are empty
        """

        return self.empty_positions

    def make_selection(self):
        """Makes the next pick

        :return:
        """

        pass
