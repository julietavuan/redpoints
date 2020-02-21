from __future__ import annotations
from abc import ABC, abstractmethod
import logging
from Issues import Issues
from Repositories import Repositories
from Wikis import Wikis


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

