"""main
Creates a fantasy football draft simulation

Author: Zach Sahlin
"""

from draft import Draft
from team import Team


def main():
    """
    main

    :return: none
    """
    draft = Draft(10)
    draft.start()
    draft.end()


main()
