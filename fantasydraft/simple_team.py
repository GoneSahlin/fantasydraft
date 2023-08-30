from fantasydraft.player import Player
from fantasydraft.team import Team

class SimpleTeam(Team):
    name = "Simple"
    
    def make_selection(self) -> Player:
        players = self.draft.get_players().copy()

        players = sorted(players, key=lambda player: player.rank)

        for player in players:
            if player.position in self.empty_positions or (player.position in self.draft.flex_options and 'FLEX' in self.empty_positions):
                if player.rank - 12 <= players[0].rank:
                    return player

        # if no players found to fill an empty position slot, select the highest rank
        return players[0]
