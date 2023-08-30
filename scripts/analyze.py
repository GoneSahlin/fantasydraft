import random
from datetime import datetime
from matplotlib import pyplot as plt
import os

from fantasydraft.simple_team import SimpleTeam
from fantasydraft.mcts_team import MCTSTeam
from fantasydraft.utils import create_teams
from fantasydraft.draft import Draft


random.seed(datetime.now().timestamp())

NUM_TEAMS = 12
TOTAL_ROUNDS = 16


# test mcts team against all simple teams

mcts_totals = []
other_totals = []

for i in range(NUM_TEAMS):
    team_types = [SimpleTeam] * NUM_TEAMS
    team_types[i] = MCTSTeam

    draft = Draft(NUM_TEAMS, TOTAL_ROUNDS, teams=None)
    teams = create_teams(draft, team_types)
    draft.teams = teams

    draft.start()

    totals = [team.calculate_total() for team in teams]

    mcts_totals.append(totals[i])
    totals.pop(i)
    other_totals.append(totals)

fig, ax = plt.subplots()

ax.scatter(x=range(1, NUM_TEAMS + 1), y=mcts_totals, c='red')

for i in range(NUM_TEAMS):
    ax.scatter(x=[i+1] * (NUM_TEAMS - 1), y=other_totals[i], c='cornflowerblue')

plt.savefig(os.path.join("media", "analysis.png"))