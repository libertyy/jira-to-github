from . import choice


def run(gh=None):
    """
    steps:
        - Ask for users or organization
        - Ask for repositories seleciton
    """

    type = choice.askType(gh)
    user = gh.get_user()

    organization = choice.askOrganisation(user, type)
