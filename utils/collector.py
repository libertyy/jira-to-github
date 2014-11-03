from utils.models import Issue


def issues(root):

    issues = []

    for issue in root:
        desc = issue.find('description').text

        if desc is None:
            desc = ''

        issues.append(Issue(issue.find('summary').text, 'Freyskeyd',
                            desc))
    return issues


def authors(root):

    authors = []

    for issue in root:
        name = issue.find('reporter').attrib.get('username').lower()

        if name not in authors:
            authors.append(name)

    return authors
