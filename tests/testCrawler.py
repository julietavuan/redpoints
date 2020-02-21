import unittest
from unittest.mock import Mock

from crawler import Crawler

def constructorMock(name):
    instance = Mock()
    instance._name_of_parent_class = name
    constructor = Mock(return_value=instance)
    return constructor

class CrawlerTes(unittest.TestCase):

    def setUp(self) -> None:
        self.github = constructorMock("GitHubConnector")
        self.crawler = Crawler(self.github)
        self.data = ["a","ruby,rails","Repositories"]

    def test_usage(self):
        self.setUp()
        result = self.crawler.usage()
        self.assertEqual("To use this crawler please send keywords divided by comma, type for the search and the proxys to use also "
              "divided by comma. For example: python3 crawler.py ruby,rails Repositories 10.0.0.19:98982,10.0.25.19:96782."
              "The Keywords must be in the form of word,word.",result)

    def test_search_ok(self):
        self.setUp()

        result = self.crawler.searchData(self.data)
        self.assertEqual(len(result),10)

if __name__ == '__main__':
    unittest.main()
