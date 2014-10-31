#!/usr/bin/env python

import xml.etree.ElementTree as ET
from utils import collector
from steps import loader
import sys
import os
from github import Github

if len(sys.argv) > 1:

    access_token = os.environ['GITHUB_ACCESS_TOKEN']
    github = Github(access_token)
    tree = ET.parse(sys.argv[1])
    root = tree.getroot()

    # collect Authors
    authors = collector.authors(root.iter('item'))

    # start steps
    loader.run(github=github)

    # for issue in root.iter('item'):
    #     print(issue.find('title').text)
else:
    print('you need to provide a file')
