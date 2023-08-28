import pandas as pd
import os

from fantasydraft.player import Player


def get_moves(draft):
    moves = []

    for pos in draft.player_pos_dict:
        players = draft.get_players(pos)
        if players:
            moves.append(players[0])

    return moves


def create_player_pos_dict(players):
    player_pos_dict = {"QB": [], "RB": [], "WR": [], "TE": [], "ST": [], "K": []}

    for player in players:
        if player.position in player_pos_dict:
            player_pos_dict[player.position].append(player)
        else:
            print(f"Incorrect position {player.position} for Player: {player.name}")

    return player_pos_dict


def create_teams(draft, team_types):
    """Creates the teams in the draft

    :param num_teams: number of teams in the league
    """
    teams = []
    for team_type in team_types:
        teams.append(team_type(draft))

    return teams


def print_rosters(draft, team_types):
    rows = []
    for i in range(draft.total_rounds):
        row = []
        for team in draft.teams:
            row.append(team.roster[i].name)
        rows.append(row)

    df = pd.DataFrame(data=rows, columns=[type.name for type in team_types])

    print(df)


def read_players():
    """Reads in the player data from a csv file
    """
    filename = os.path.join("data", "players.csv")

    player_df = pd.read_csv(filename)

    players = []
    for _, row in player_df.iterrows():
        players.append(Player(row['name'], row['position'], row['points'], row['rank']))

    players = sorted(players, key=lambda x: x.points, reverse=True)

    return players
