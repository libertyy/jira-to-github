#!/usr/bin/env python3

import xml.etree.ElementTree as ET
from github import Github

tree = ET.parse('SearchRequest.xml')
root = tree.getroot()

for issue in root.iter('item'):
    print( issue.find('title').text.encode('utf-8') )