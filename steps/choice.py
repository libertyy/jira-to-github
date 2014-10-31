

def askRepository(source):
    """
    Propose repository selection
    """

    selected_repo = None

    repositories = []

    source_repo = source.get_repos()

    for repo in source_repo:
        print(repo.name)
        repositories.append(repo.name)

    while selected_repo not in repositories:
        selected_repo = input('>> ').lower()

    for repo in source_repo:
        if repo.name.lower() == selected_repo:
            selected_repo = repo

    return selected_repo


def askOrganization(ep, type):
    """
    Propose user's organization
    """

    organization = None

    if type is 'organization':
        orgs_login = []

        orgs = ep.get_orgs()

        for org in orgs:
            print(org.login)
            orgs_login.append(org.login.lower())

        while organization not in orgs_login:
            organization = input('>> ').lower()

        for org in orgs:
            if org.login.lower() == organization:
                organization = org

    return organization


def askType(gh):
    """
    Ask for interaction source type
    """

    print('Do you want to import issue for your (p)ersonal profil or an \
(o)rganization ?')

    type = None

    options = ['p', 'personal', 'o', 'orga', 'organization']

    while type not in options:
        type = input('>> ').lower()

    if type in ['p', 'personal']:
        type = 'user'
    else:
        type = 'organization'

    return type
