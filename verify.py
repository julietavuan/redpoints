

class Verify:

    def __init__(self):
        self.types = ["Repositories", "Issues", "Wikis"]

    def verifiedType(self, type):
        return type in self.types

    def verifyKeywords(self, keywords):
        return isinstance(keywords, str)

    def verifyParams(self, args):
        if self.verifyKeywords(args[1]):
            if self.verifiedType(args[2]):
                return True
            else:
                print("There is an error in the type of search. Please send Repositories, Issues or Wikis")
                return False
        else:
            print("There is an error in the Keywords. Please send words divided by commas in unicode type.")
            return False


