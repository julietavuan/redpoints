import unittest
import os
from bs4 import BeautifulSoup
from issues import Issues

class IssuesTest(unittest.TestCase):
    def testIssuesParseOk(self):
        dir = os.path.dirname(__file__)
        filename = os.path.join(dir, "mocks", "issues-result-ok.html")
        text = open(filename)
        soup = BeautifulSoup(text, "html.parser")
        text.close()
        issues = Issues()
        i = issues.search_gitHub_data(soup)
        self.assertEqual(i[0]["url"],'https://github.com/simple-icons/simple-icons/issues/2385')
        self.assertEqual(len(i), 10)


if __name__ == '__main__':
    unittest.main()
