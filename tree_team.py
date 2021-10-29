from team import Team


class TreeTeam(Team):
    """
    """

    def __init__(self):
        """
        """
        pass

    def make_selection(self):
        """Makes a selection using a tree algorithm.
        """
        current_state = self.draft.get_players()
        
        pass

    def create_tree(self):
        """Creates a tree of all possible picks
        """
        pass

    class TreeNode:
        """A node in the tree
        """

        def __init__(self, state):
            """
            """
            self.state = state
