
def askOrganization(ep, type):
    """
    Propose user's organization
    """

    organization = None

    if type is 'organization':
        orgs_login = []

        for org in ep.get_orgs():
            print(org.login)
            orgs_login.append(org.login.lower())

        while organization not in orgs_login:
            organization = input('>> ').lower()

    return organization


def askType(gh):
    """
    Ask for interaction source type
    """

    print('Do you want to import issue for your personal profil or an \
organization ?')

    type = None

    options = ['p', 'personal', 'o', 'orga', 'organization']

    while type not in options:
        type = input('>> ').lower()

    if type in ['p', 'personal']:
        type = 'user'
    else:
        type = 'organization'

    return type
