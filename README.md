##
Current: 1.0.0
## How to use

First you need to generate an `ACCESS_TOKEN` in your personal profil.

then, create a virtualenv with python 3.4.

```
GITHUB_ACCESS_TOKEN=YOU_TOKEN ./run.py YOUFILE.xml
```

## Roadmap

### Sprint1 - Release 1.0

Organization importation first, we need to be able to select an organization, a repository to be used and add issues to
this repository.

### Sprint2 - Release 1.1

Only selection of an empty repository.

Create missing issue to keep issue number clear

Import milestones and labels

### Sprint3 - Release 1.2

Create issue with correct labels and milestone

Parse description to replace JIRA mention with Github mention

### Sprint4 - Release 1.3

Autocompletion on selection

