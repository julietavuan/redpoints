import unittest
import os
from bs4 import BeautifulSoup
from Issues import Issues

class IssuesTest(unittest.TestCase):
    def testIssuesParseOk(self):
        dir = os.path.dirname(__file__)
        filename = os.path.join(dir, "mocks", "issues-result-ok.html")
        text = open(filename)
        soup = BeautifulSoup(text, "html.parser")
        text.close()
        issues = Issues()

        i = issues.search_gitHub_data(soup)
        self.assertEqual(len(i), 10)


if __name__ == '__main__':
    unittest.main()
