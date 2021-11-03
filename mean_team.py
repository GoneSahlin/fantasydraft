from team import Team


class MeanTeam(Team):
    """Chooses players based on how it will affect the mean of potential future picks
    """

    def __init__(self, draft, pos_list, team_number):
        """Constructor
        """
        super().__init__(draft, pos_list, team_number)

    def make_selection(self):
        """Makes the next pick
        """
        pass

    def make_matrix(self):
        """Makes a matrix of projected picks
        """
        pick_list = self.calculate_pick_numbers()
        matrix = []
        for i in range(len(self.empty_positions)):
            pick_number = pick_list[i + self.draft.round]
            row = []
            for pos in self.empty_positions:

                # find index of player and their projected total points
                player = (index, points)
                row.append(player)
            matrix.append(row)

    def calculate_pick_numbers(self):
        """Calculates the pick numbers for future picks
        """
        pick_list = []
        for i in range(len(self.draft.pos_list)):
            if self.draft.round % 2 == 0:
                pick_list.append(self.draft.round * self.draft.num_teams + self.team_number)
            else:
                pick_list.append((self.draft.round + 1) * self.draft.num_teams - self.team_number) # TODO check

        return pick_list
