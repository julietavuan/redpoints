from __future__ import annotations
from abc import ABC, abstractmethod

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
        return FactoryTypes.factory[gitHubType]

