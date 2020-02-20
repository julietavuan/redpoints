from __future__ import annotations
from abc import ABC, abstractmethod


class Strategy(ABC):

    @abstractmethod
    def search_gitHub_data(self, soup):
        pass