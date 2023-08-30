"""main
Creates a fantasy football draft simulation

Author: Zach Sahlin
"""
import os
import random
from datetime import datetime

from draft import Draft
from mcts_team import MCTSTeam
from simple_team import SimpleTeam
from user_team import UserTeam
from utils import create_teams, print_rosters


def main():
    """
    main

    :return: none
    """
    random.seed(datetime.now().timestamp())

    team_types = []
    for _ in range(6):
        team_types.append(UserTeam)
    for _ in range(1):
        team_types.append(MCTSTeam)
    for _ in range(5):
        team_types.append(UserTeam)

    for i in range(1):
        draft = Draft(12, 16, teams=None)
        teams = create_teams(draft, team_types)
        draft.teams = teams

        draft.start()
        draft.end()

        filename = os.path.join("data", f"roster_{i}.csv")
        print_rosters(draft, team_types, filename)


main()
