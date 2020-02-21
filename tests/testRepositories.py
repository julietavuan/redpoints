import unittest
from  bs4 import BeautifulSoup
import os
from repositories import Repositories


class RepositoriesTest(unittest.TestCase):

    def testRepositoriesParseOk(self):
        dir = os.path.dirname(__file__)
        filename = os.path.join(dir, "mocks","repositories-result-ok.html")
        text = open(filename)
        soup = BeautifulSoup(text, "html.parser")
        text.close()
        repositories = Repositories()

        r = repositories.search_gitHub_data(soup)
        self.assertEqual(len(r),10)

if __name__ == '__main__':
    unittest.main()
