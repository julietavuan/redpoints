import unittest


class CrawlerTes(unittest.TestCase):
    def test_something(self):
        self.assertEqual(True, False)

    def testVerifyParamsOk(self): pass

    def testVerifyParamsWrongKeyWords(self):pass

    def testVerifyParamsWrongType(self):pass

    def testSearchDataOk(self):pass

    def testSearchDataNoMatches(self):pass

    def testSearchDataWrongInstanceFactory(self):pass

    def testSearchDataWrongStrategy(self):pass

    def testSearchDataWrongProxys(self):pass

    def testSearchDataWrongURL(self):pass

    def testSearchDataWrongGitHubResponse(self):pass

    def testSearchDataWrongStrategyParse(self):pass

if __name__ == '__main__':
    unittest.main()
