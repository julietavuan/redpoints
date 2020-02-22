import unittest
import os
from bs4 import BeautifulSoup
from wikis import Wikis


class WikisTest(unittest.TestCase):
    def testWikisParseOk(self):
        dir = os.path.dirname(__file__)
        filename = os.path.join(dir, "mocks", "wikis-result-ok.html")
        text = open(filename)
        soup = BeautifulSoup(text, "html.parser")
        text.close()
        wikis = Wikis()
        w = wikis.search_gitHub_data(soup)
        self.assertEqual(w[0]["url"],'https://github.com//xuanrljp/genba/wiki/Ruby&Rails')
        self.assertEqual(len(w), 10)


if __name__ == '__main__':
    unittest.main()
