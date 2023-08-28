from mcts import mcts

from player import Player
from team import Team
from utils import get_moves


class State():
    def __init__(self, draft, max_team_index):
        self.draft = draft
        self.max_team_index = max_team_index

    
    def copy(self):
        new_draft = self.draft.copy()

        new_state = State(new_draft, max_team_index=self.max_team_index)

        return new_state


    def getCurrentPlayer(self):
        """Returns 1 if it is the maximizer player's turn to choose an action, or -1 for the minimiser player
        """
        if self.draft.cur_team_index == self.max_team_index:
            return 1
        else:
            return -1

    def getPossibleActions(self):
        """Returns an iterable of all actions which can be taken from this state
        """
        moves = get_moves(self.draft)

        return moves

    def takeAction(self, action):
        """Returns the state which results from taking action action
        """
        new_state = self.copy()

        new_state.draft.draft_player(action)

        return new_state        
        

    def isTerminal(self):
        """Returns True if this state is a terminal state
        """
        return self.draft.is_draft_over()

    def getReward(self):
        """Returns the reward for this state. Only needed for terminal states.
        """
        scores = []
        for team in self.draft.teams:
            scores.append(team.calculate_total())

        winner_index = scores.index(max(scores))

        if winner_index == self.max_team_index:
            return True
        
        return False


class MCTSTeam(Team):

    def make_selection(self) -> Player:
        initialState = State(self.draft, self.draft.cur_team_index)
        searcher = mcts(timeLimit=1000)
        action = searcher.search(initialState=initialState)

        return action
