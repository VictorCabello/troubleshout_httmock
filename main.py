#!/usr/bin/env python
"""
This is only a test of how to use
requests module and multiprocessing
"""
import os, traceback
import requests
from multiprocessing import Pool

def getowner(repo):
    owner = repo['owner']['login']
    r = requests.get("https://api.github.com/users/{0}".format(owner))
    return "{repo} ({owner})".format(repo=repo['name'], owner=r.json()['login'])

def main():
    r = requests.get('https://api.github.com/orgs/octokit/repos')
    repos = [repo for repo in r.json()]
    p = Pool(4)
    print p.map(getowner, repos)

if __name__ == '__main__':
    try:
        main()
    except Exception, e:
        print str(e)
        traceback.print_exc()
        os._exit(1)
