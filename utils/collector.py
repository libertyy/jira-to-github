
def authors(root):

    authors = []

    for issue in root:
        name = issue.find('reporter').attrib.get('username').lower()

        if name not in authors:
            authors.append(name)

    return authors
