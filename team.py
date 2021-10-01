"""team
A fantasy football team

Author: Zach Sahlin
"""


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
        player_pos = self.draft.get_players()['Position'][player_rank]
        if player_pos in self.empty_positions:
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

        draftable_players = self.draft.get_players()[~self.draft.get_players()['Picked']]

        for index, row in draftable_players.iterrows():
            if row['Position'] in self.empty_positions:
                return index
