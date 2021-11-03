"""team
A fantasy football team

Author: Zach Sahlin
"""

import pandas as pd
from collections import OrderedDict


class Team:
    """A fantasy football team
    """
    def __init__(self, draft, pos_list, team_number):
        """Constructor"""

        self.draft = draft
        self.my_players_df = pd.DataFrame()
        self.empty_positions = pos_list.copy()
        self.team_number = team_number

    def add_player(self, player_rank):
        """adds a player to the team

        :param player_rank: the rank of the player to add
        """
        if player_rank in self.draft.get_players().index:
            self.my_players_df = self.my_players_df.append(self.draft.get_players().loc[player_rank, :])
        else:
            self.my_players_df = self.my_players_df.append(self.draft.get_players().loc[0, :])
            return

        player_pos = self.draft.get_players()['Position'][player_rank]
        if player_pos in self.empty_positions:
            self.empty_positions.remove(player_pos)
        elif player_pos in ('RB', 'WR') and 'FLEX' in self.empty_positions:
            self.empty_positions.remove('FLEX')

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
            elif row['Position'] in ('RB', 'WR') and 'FLEX' in self.empty_positions:
                return index

        # if no players that fit lineup
        first_index = draftable_players.index[0]
        return first_index


    def calculate_total(self):
        """Calculates the total projected points

        :returns total_points: the total projected points for all starting players
        """
        def find_best_player(pos, benched_players_df):
            """Finds the best player with the position

            :param pos: Position code
            :param benched_players_df: DataFrame of players on the bench
            :returns selected_player_rank: the rank of the best player with the position
            """

            flex_set = {'RB', 'WR'}
            if pos in set(benched_players_df['Position']):
                pos_players_df = benched_players_df.groupby('Position').get_group(pos).copy()
            elif pos == 'FLEX' and not flex_set.isdisjoint(set(benched_players_df['Position'])):
                pos_players_df = pd.DataFrame(columns=benched_players_df.keys())
                pos_groupby = benched_players_df.groupby('Position')
                for position in flex_set:
                    if position in list(benched_players_df['Position']):
                        pos_players_df = pd.concat([pos_players_df, pos_groupby.get_group(position)])
            else:
                return 0

            pos_players_df = pos_players_df.sort_values(by=['Total pts'], ascending=False)
            return pos_players_df.iloc[0, :].name

        pos_set = list(OrderedDict.fromkeys(self.draft.pos_list))
        if 'FLEX' in pos_set:
            pos_set.append(pos_set.pop(pos_set.index('FLEX')))

        benched_players_df = self.my_players_df
        starting_players_df = pd.DataFrame()

        for pos in pos_set:
            for i in range(self.draft.pos_list.count(pos)):
                selected_player_rank = find_best_player(pos, benched_players_df)
                if selected_player_rank != 0:
                    starting_players_df = starting_players_df.append(benched_players_df.loc[selected_player_rank, :])
                    benched_players_df = benched_players_df.drop([selected_player_rank])
                else:
                    starting_players_df = starting_players_df.append(self.draft.get_players().loc[0, :])

        total_points = starting_players_df['Total pts'].sum()

        return total_points



