from __future__ import annotations
from abc import ABC, abstractmethod
import logging
from issues import Issues
from repositories import Repositories
from wikis import Wikis


class FactoryTypes(ABC):

    factory = {}
    factory["Repositories"] = Repositories()
    factory["Issues"] = Issues()
    factory["Wikis"] = Wikis()

    @classmethod
    def factory_method(self, gitHubType):
        if gitHubType in FactoryTypes.factory.keys():
            return FactoryTypes.factory[gitHubType]
        else:
            return None

