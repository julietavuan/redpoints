import unittest
from  bs4 import BeautifulSoup
import os
from repositories import Repositories


class RepositoriesTest(unittest.TestCase):

    def setUp(self) -> None:
        dir = os.path.dirname(__file__)
        filename = os.path.join(dir, "mocks", "repositories-result-ok.html")
        text = open(filename)
        self.soup = BeautifulSoup(text, "html.parser")
        text.close()
        self.repositories = Repositories()

    def testRepositoriesParseOk(self):
        self.setUp()
        r = self.repositories.search_gitHub_data(self.soup)
        self.assertEqual(r[0]["url"],"https://github.com/rails/rails")
        self.assertEqual(len(r),10)

    def testRepositoriesBonus(self):
        self.setUp()
        url = "https://github.com/OLIMEX/OLINUXINO"
        r = self.repositories.get_repository_data(url)
        self.assertEqual(r["extra"]["owner"],"OLIMEX")

if __name__ == '__main__':
    unittest.main()
