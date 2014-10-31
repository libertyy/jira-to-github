from utils.models import Issue
from . import choice


def run(gh=None):
    """
    steps:
        - Ask for users or organization
        - Ask for repositories seleciton
        - Add one issue
    """

    type = choice.askType(gh)
    user = gh.get_user()

    organization = choice.askOrganization(user, type)

    repository = choice.askRepository(organization if organization else user)

    issue = Issue('Title', 'Freyskeyd', 'content')

    issue.add_to_repository(repository)

