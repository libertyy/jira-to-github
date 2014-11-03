from . import choice
from utils import collector


def run(gh=None, xml=None):
    """
    steps:
        - Ask for users or organization
        - Ask for repositories seleciton
        - Add one issue
    """

    type = choice.askType(gh)
    user = gh.get_user()

    organization = choice.askOrganization(user, type)

    source = organization if organization else user

    repository = choice.askRepository(source)

    issues = collector.issues(xml.iter('item'))

    for i in issues:
        i.add_to_repository(repository)
