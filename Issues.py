from Strategy import Strategy
import json

class Issues(Strategy):

    def search_gitHub_data(self, soup):
        url_issues = []
        issues = soup.findAll("div", {"class": "f4 text-normal"})
        for issue in issues:
            a = issue.contents[1].attrs["data-hydro-click"]
            data_hydro = json.loads(a)
            url = {"url":data_hydro['payload']['result']['url']}
            url_issues.append(url)
        return url_issues
