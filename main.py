#!/usr/bin/env python
"""
This is only a test of how to use
requests module and multiprocessing
"""
import os

def main():
    print 'hello'

if __name__ == '__main__':
    try:
        main()
    except Exception, e:
        print str(e)
        traceback.print_exc()
        os.__exit(1)