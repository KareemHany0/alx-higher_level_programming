#!/usr/bin/python3
'''Get GitHub credentials (username and password)
   and uses the GitHub API to display your id
'''
import requests
from requests.auth import HTTPBasicAuth
from sys import argv


req = requests.get('https://api.github.com', auth=(argv[1], argv[2]))
print(req.json().get('id'))