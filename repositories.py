from strategy import Strategy
import json
import requests
from bs4 import BeautifulSoup

class Repositories(Strategy):

    def get_name(self):
        return("Repositories")

    def search_gitHub_data(self, soup):
        repos = []
        repositories = soup.findAll("a", {"class": "v-align-middle"})
        for link in repositories:
            data_hydro = link.attrs["data-hydro-click"]
            data_hydro = json.loads(data_hydro)
            repository_data = self.get_repository_data(data_hydro['payload']['result']['url'])
            repos.append(repository_data)
        return repos

    def get_repository_data(self, url):
        data = {}
        data["url"] = url
        result = requests.get(url)
        soup = BeautifulSoup(result.text, "html.parser")
        data["extra"] = {}
        data["extra"]["owner"] = soup.find("a", {"rel":"author"}).text
        data["extra"]["language_stats"] = {}
        languages = soup.findAll("span", {"class": "language-color", "itemprop": "keywords"})
        for language in languages:
            l = language.get("aria-label").split(" ")
            data["extra"]["language_stats"][l[0]] =l[1]
        return data

