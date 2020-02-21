#! /usr/bin/env python3
import requests
import sys
from lxml.html import fromstring
from itertools import cycle

from FactoryTypes import FactoryTypes
from Type import Type


url = "https://github.com/search?q={}&type={}"
types = ["Repositories","Issues", "Wikis"]

# TO DO, help documentation
# list of proxys
# keywords
# type
def usage():
    print("To use this crawler please send keywords divided by comma, type for the search and the proxys to use also "
          "divided by comma. For example: python3 crawler.py ruby,rails Repositories 10.0.0.19:98982,10.0.25.19:96782")

def get_proxies():
    url = 'https://free-proxy-list.net/'
    response = requests.get(url)
    parser = fromstring(response.text)
    proxies = set()
    for i in parser.xpath('//tbody/tr')[:10]:
        if i.xpath('.//td[7][contains(text(),"yes")]'):
            proxy = ":".join([i.xpath('.//td[1]/text()')[0], i.xpath('.//td[2]/text()')[0]])
            proxies.add(proxy)
    return proxies

def get_content(github_url):
    proxies = get_proxies()
    proxy_pool = cycle(proxies)
    for i in range(1, 11):
        proxy = next(proxy_pool)
        try:
            response = requests.get(github_url, proxies={"http://" + proxy : "https://" + proxy})
            if response.status_code == 200:
                return response.text
        except Exception as e:
            print(str(e))

def url_format(words, url):
    keywords= words[1].replace(",","+")
    return url.format(keywords,words[2])

def searchData(data, url):
    try:
        gitHubType = FactoryTypes.factory_method(data[2])
        type = Type(gitHubType)
        data = type.searchParams(get_content(url_format(data,url)))
        print(data)
    except Exception as e:
        print(str(e))
        usage()

def verifiedType(type):
    return type in types

def verifyKeywords(keywords):
    return isinstance(keywords,str)

def verifyParams(args):
    return (verifyKeywords(args[1]) and verifiedType(args[2]))



if __name__ == '__main__':
    if len(sys.argv)== 3:
        if verifyParams(sys.argv):
            searchData(sys.argv, url)
    else:
        usage()







