#! /usr/bin/env python3

import sys
from factoryTypes import FactoryTypes
from type import Type
from gitHubConnector import GitHubConnector
from verify import Verify


class Crawler:

    def __init__(self, github):
        self.github = github

    def usage(self):
        return ("To use this crawler please send keywords divided by comma and type for the search."
                "We handle de proyis ;). For example: python3 crawler.py ruby,rails Repositories"
                "The Keywords must be in the form of word,word.")


    def searchData(self,data):
        try:
            gitHubType = FactoryTypes.factory_method(data[2])
            type = Type(gitHubType)
            return type.searchParams(self.github.get_content(data))
        except Exception as e:
            print(str(e))
            self.usage()


if __name__ == '__main__':
    crawler = Crawler(GitHubConnector())
    if len(sys.argv)== 3:
        verify = Verify()
        if verify.verifyParams(sys.argv):
            print (crawler.searchData(sys.argv))

    else:
        print(crawler.usage())







