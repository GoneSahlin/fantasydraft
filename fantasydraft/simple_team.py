from fantasydraft.player import Player
from team import Team

class SimpleTeam(Team):
    def make_selection(self) -> Player:
        players = self.draft.get_players().copy()

        players = sorted(players, key=lambda player: player.rank)

        for player in players:
            if player.position in self.empty_positions:
                return player
            elif player.position in ('RB', 'WR') and 'FLEX' in self.empty_positions:
                return player

        # if no players found to fill an empty position slot, select the highest rank
        return players[0]
