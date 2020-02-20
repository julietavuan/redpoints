from Strategy import Strategy
import json

class Repositories(Strategy):

    def search_gitHub_data(self, soup):
        repos = []
        repositories = soup.findAll("a", {"class": "v-align-middle"})
        for link in repositories:
            data_hydro = link.attrs["data-hydro-click"]
            data_hydro = json.loads(data_hydro)
            url = {"url":data_hydro['payload']['result']['url']}
            repos.append(url)
        return repos
