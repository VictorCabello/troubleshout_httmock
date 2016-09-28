import unittest
from httmock import urlmatch, HTTMock, all_requests, response
from main import main

class TestSuite (unittest.TestCase):

    def test_01(self):
        with HTTMock(response_content):
            main()


@all_requests
def response_content(url, request):
    print url.path
    headers = {'content-type': 'application/json',
               'Set-Cookie': 'foo=bar;'}
    if url.path == '/orgs/octokit/repos':
        content = [
            { 'name':'mycoolrepo', 'owner': { 'login':'victor'}}
        ]
        return response(203, content, headers, None, 5, request)
    else:
        content = { 'login':'victor'}
        return response(203, content, headers, None, 5, request)

