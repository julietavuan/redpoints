#! /usr/bin/env python3

import sys
from factoryTypes import FactoryTypes
from type import Type
from gitHubConnector import GitHubConnector
from verify import Verify


class Crawler:

    def github_setter(self, github):
        self.github = github

    def usage(self):
        return ("To use this crawler please send keywords divided by comma, type for the search and the proxys to use also "
              "divided by comma. For example: python3 crawler.py ruby,rails Repositories 10.0.0.19:98982,10.0.25.19:96782."
              "The Keywords must be in the form of word,word.")


    def searchData(self,data):
        try:
            gitHubType = FactoryTypes.factory_method(data[2])
            type = Type(gitHubType)
            self.github_setter(GitHubConnector())
            return type.searchParams(self.github.get_content(data))
        except Exception as e:
            print(str(e))
            self.usage()


if __name__ == '__main__':
    crawler = Crawler()
    if len(sys.argv)== 3:
        verify = Verify()
        if verify.verifyParams(sys.argv):
            print (crawler.searchData(sys.argv))
    else:
        print(crawler.usage())







