from __future__ import annotations
from strategy import Strategy
from bs4 import BeautifulSoup

class Type:


    def __init__(self, strategy: Strategy) -> None:
        self._strategy = strategy

    @property
    def strategy(self) -> Strategy:
        return self._strategy

    @strategy.setter
    def strategy(self, strategy: Strategy) -> None:
        self._strategy = strategy

    def searchParams(self, html):
        soup = BeautifulSoup(html, 'html.parser')
        if len(soup.find_all("div",{"class":"blankslate"})) > 0:
            print("There isn't an output with the specific search. Please try again")
            return {"url":"None"}
        else:
            return self._strategy.search_gitHub_data(soup)