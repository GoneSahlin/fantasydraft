"""main
Creates a fantasy football draft simulation

Author: Zach Sahlin
"""
import os

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
    team_types = []

    # for _ in range(1):
    #     team_types.append(MCTSTeam)
    # for _ in range(11):
    #     team_types.append(SimpleTeam)

    for _ in range(12):
        team_types.append(SimpleTeam)

    draft = Draft(12, 16, teams=None)
    teams = create_teams(draft, team_types)
    draft.teams = teams


    draft.start()
    draft.end()

    print_rosters(draft, team_types)


main()
