import unittest

from crawler import Crawler
from unittest.mock import MagicMock
from gitHubConnector import GitHubConnector
import os

class CrawlerTes(unittest.TestCase):

    def setUp(self):

        self.data = ["a","ruby,rails","Repositories"]

    def test_usage(self):
        self.setUp()
        github = GitHubConnector()
        crawler = Crawler(github)
        result = crawler.usage()
        self.assertEqual("To use this crawler please send keywords divided by comma and type for the search."
                         "We handle de proyis ;). For example: python3 crawler.py ruby,rails Repositories"
                         "The Keywords must be in the form of word,word.",result)

    def test_search_ok(self):
        github = GitHubConnector()
        dir = os.path.dirname(__file__)
        filename = os.path.join(dir, "mocks", "repositories-result-ok.html")
        text = open(filename)
        github.get_content = MagicMock(return_value=text)
        crawler = Crawler(github)
        result = crawler.searchData(self.data)
        text.close()
        self.assertEqual(len(result),10)

if __name__ == '__main__':
    unittest.main()
