#!/usr/bin/env python

import xml.etree.ElementTree as ET
from utils import collector
# from github import Github

tree = ET.parse('SearchRequest.xml')
root = tree.getroot()

# collect Authors
authors = collector.authors(root.iter('item'))
print(authors)
# for issue in root.iter('item'):
#     print(issue.find('title').text)
