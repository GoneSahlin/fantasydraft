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

        def __init__(self, players, empty_pos, depth, parent):
            """
            """
            self.players = players
            self.empty_pos = empty_pos
            self.depth = depth
            self.parent = parent
            self.children = []

        def create_children(self, draft):
            """Create the children of this node
            """
            unique_pos = [pos for n, pos in enumerate(self.empty_pos) if pos not in self.empty_pos[:n]]
            for pos in unique_pos:
                # find best player in position
                player_index = self.players.groupby('Position').get_group(pos).head(1).index

                print(player_index)


                # create a child

                child = self.__class__()

                self.children.append(child)


