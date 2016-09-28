#!/usr/bin/env python
"""
This is only a test of how to use
requests module and multiprocessing
"""
import os, traceback
import requests

def main():
    r = requests.get('https://api.github.com/orgs/octokit/repos')
    list = r.json()
    for item in list:
        owner = item['owner']['login']
        next_r = requests.get("https://api.github.com/users/{0}".format(owner))
        print "{name} ({owner})".\
            format(name=item['name'], owner=next_r.json()['login'])

if __name__ == '__main__':
    try:
        main()
    except Exception, e:
        print str(e)
        traceback.print_exc()
        os._exit(1)
