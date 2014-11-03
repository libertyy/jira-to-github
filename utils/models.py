
class Issue:

    def __init__(self, title, author, body):
        self.title = title
        self.author = author
        self.body = body

    def add_to_repository(self, repo):
        repo.create_issue(self.title,
                          body=self.body,
                          assignee=self.author)
