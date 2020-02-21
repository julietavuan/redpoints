#! /usr/bin/env python3

import sys
from FactoryTypes import FactoryTypes
from Type import Type
from GitHubConnector import GitHubConnector
from Verify import Verify




def usage():
    print("To use this crawler please send keywords divided by comma, type for the search and the proxys to use also "
          "divided by comma. For example: python3 crawler.py ruby,rails Repositories 10.0.0.19:98982,10.0.25.19:96782")


def searchData(data):
    try:
        gitHubType = FactoryTypes.factory_method(data[2])
        type = Type(gitHubType)
        github = GitHubConnector()
        data = type.searchParams(github.get_content(data))
        print(data)
    except Exception as e:
        print(str(e))
        usage()


if __name__ == '__main__':
    if len(sys.argv)== 3:
        verify = Verify()
        if verify.verifyParams(sys.argv):
            searchData(sys.argv)
    else:
        usage()







