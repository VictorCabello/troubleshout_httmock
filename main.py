#!/usr/bin/env python
"""
This is only a test of how to use
requests module and multiprocessing
"""
import os, traceback
import requests
from functools import partial
from multiprocessing import Pool

def getowner(repo, otherdata):
    owner = repo['owner']['login']
    r = requests.get("https://api.github.com/users/{0}".format(owner))
    return "{repo} ({owner}) -> {other}".\
        format(
            repo=repo['name'],
            owner=r.json()['login'],
            other=otherdata
        )

def main():
    r = requests.get('https://api.github.com/orgs/octokit/repos')
    repos = [repo for repo in r.json()]
    p = Pool(4)
    func = partial(getowner, otherdata='test')
    messages =  p.map(func, repos)

    return messages

if __name__ == '__main__':
    try:
        result = main()
        for item in result:
            print item
    except Exception, e:
        print str(e)
        traceback.print_exc()
        os._exit(1)
