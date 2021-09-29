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

    def add_player(self):
        """Adds a player to the team

        :return:
        """

        pass

    def get_unfilled_positions(self):
        """Gets the positions that haven't been filled yet

        :returns unfilled_positions: the positions on the team that are empty
        """

        pass

    def make_selection(self):
        """Makes the next pick

        :return:
        """

        pass
