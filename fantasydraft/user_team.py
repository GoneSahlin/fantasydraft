from fantasydraft.player import Player
from fantasydraft.team import Team

class UserTeam(Team):
    def make_selection(self) -> Player:
        while True:
            player_name = input("Enter player name to draft: ")

            for player in self.draft.players:
                if player.name == player_name:
                    return player
        
            print("Invalid player name.")

