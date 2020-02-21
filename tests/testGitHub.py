import unittest
from gitHubConnector import GitHubConnector

class TestGitHub(unittest.TestCase):
    def setUp(self):
        self.github=GitHubConnector()
        self.words = ["a","ruby,rails","Repositories"]

    def test_url_format_ok(self):
        self.setUp()
        result =self.github.url_format(self.words)
        self.assertEqual('https://github.com/search?q=ruby+rails&type=Repositories',result)

    def test_get_content_ok(self):
        self.setUp()
        result = self.github.get_content(self.words)
        self.assertIsInstance(result,str)

    def test_get_content_wrong(self):
        self.setUp()
        words = ["a","lskdlskdjdl,alskjdlkasjd","Repositories"]
        result = self.github.get_content(words)
        self.assertIsInstance(result,str)

if __name__ == '__main__':
    unittest.main()
