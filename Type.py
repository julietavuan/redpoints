from __future__ import annotations
from Strategy import Strategy
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
        return self._strategy.search_gitHub_data(soup)