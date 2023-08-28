# from matplotlib import pyplot as plt

from fantasydraft.utils import read_players


players = read_players()

# plt.plot()

# def violin_plots():


#     df_std = (df - train_mean) / train_std
    # df_std = df_std.melt(var_name='Column', value_name='Normalized')
    # plt.figure(figsize=(12, 6))
    # ax = sns.violinplot(x='Column', y='Normalized', data=df_std)
    # _ = ax.set_xticklabels(df.keys(), rotation=90)