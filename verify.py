

class Verify:

    def __init__(self):
        self.types = ["Repositories", "Issues", "Wikis"]

    def verifiedType(self, type):
        return type in self.types

    def verifyKeywords(self, keywords):
        return isinstance(keywords, str)

    def verifyParams(self, args):
        return self.verifyKeywords(args[1]) and self.verifiedType(args[2])