from player import Player


def get_moves(draft):
        moves = []

        for pos in draft.player_pos_dict:
            moves.append(draft.player_pos_dict[pos][0])

        return moves


def create_player_pos_dict(players):
    player_pos_dict = {"QB": [], "RB": [], "WR": [], "TE": [], "ST": [], "K": []}

    for player in players:
        if player.position in player_pos_dict:
            player_pos_dict[player.position].append(player)
        else:
            print(f"Incorrect position {player.position} for Player: {player.name}")

    return player_pos_dict
