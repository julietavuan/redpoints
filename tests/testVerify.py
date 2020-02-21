import unittest
from Verify import Verify

class TestVerify(unittest.TestCase):

    def set_up(self):
        self.verify = Verify()

    def testKeywordsOk(self):
        self.set_up()
        result = self.verify.verifiedType("Issues")
        self.assertEqual(True,result)

    def testKeywordsWrong(self):
        self.set_up()
        a = "a".encode("ascii")
        result = self.verify.verifiedType(a)
        self.assertEqual(False,result)

    def testVerifyParamsOk(self):
        self.set_up()
        data = ['/RedPoints/crawler.py', 'ruby,rails', 'Issues']
        result = self.verify.verifyParams(data)
        self.assertEqual(True,result)

    def testVerifyParamsWrong(self):
        self.set_up()
        data = ['/RedPoints/crawler.py', 'ruby,rails', 'olo']
        result = self.verify.verifyParams(data)
        self.assertEqual(False,result)

    def testVerifiedTypeOk(self):
        self.set_up()
        result = self.verify.verifiedType("Repositories")
        self.assertEqual(True,result)

    def testVerifiedTypeWrong(self):
        self.set_up()
        result = self.verify.verifiedType("XX")
        self.assertEqual(False,result)

if __name__ == '__main__':
    unittest.main()
