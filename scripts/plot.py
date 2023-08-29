from matplotlib import pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np
import os

from fantasydraft.utils import read_players, create_player_pos_dict


players = read_players()
player_pos_dict = create_player_pos_dict(players)


def violin_plots():
    fig, ax = plt.subplots()

    data = []
    xs = range(6)
    amounts = {"QB": 24, "RB": 36, "WR": 36, "TE": 24, "ST": 24, "K": 24}
    for position in player_pos_dict:
        points_list = [player.points for player in player_pos_dict[position]]

        # clean points list
        points_list = sorted(points_list, reverse=True)
        points_list = points_list[:amounts[position]]

        mean = np.mean(points_list)
        std = np.std(points_list)

        points_list = [(points - mean) / 25 for points in points_list]

        data.append(points_list)

    ax = sns.violinplot(data)
    _ = ax.set_xticklabels(player_pos_dict.keys())
    

    filepath = os.path.join("media", "violinplot.png")

    plt.savefig(filepath)


def main():
    violin_plots()


if __name__ == "__main__":
    main()