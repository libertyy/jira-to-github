from . import choice


def run(github=None):
    """
    steps:
        - Ask for users or organisation
        - Ask for repositories seleciton
    """

    type = choice.askType(github)
    print(type)
