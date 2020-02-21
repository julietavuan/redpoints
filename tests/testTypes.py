import unittest
import os
from Repositories import Repositories
from Type import Type

class TypesTest(unittest.TestCase):

    def testParseOk(self):
        dir = os.path.dirname(__file__)
        filename = os.path.join(dir, "mocks","repositories-result-ok.html")
        text = open(filename)
        strategy = Repositories()
        strategyType = Type(strategy)
        response =strategyType.searchParams(text)
        self.assertEqual(len(response),10)

    def testParseWrong(self):
        dir = os.path.dirname(__file__)
        filename = os.path.join(dir, "mocks","repositories-result-wrong.html")
        text = open(filename)
        strategy = Repositories()
        strategyType = Type(strategy)
        response =strategyType.searchParams(text)
        self.assertEqual(len(response),0)

if __name__ == '__main__':
    unittest.main()
