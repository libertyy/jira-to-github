

def askType(gh):
    """
    Ask for interaction source type
    """

    print('Do you want to import issue for your personal profil or an \
organisation ?')

    type = None

    options = ['p', 'personal', 'o', 'orga', 'organisation']

    while type not in options:
        type = input('>> ').lower()

    if type in ['p', 'personal']:
        type = 'user'
    else:
        type = 'organisation'
    return type
