import unittest
from unittest.mock import Mock
import factoryTypes


def constructorMock(name):
    instance = Mock()
    instance._name_of_parent_class = name
    constructor = Mock(return_value=instance)
    return constructor

class FactoryTest(unittest.TestCase):

    def setUp(self):
        factoryTypes.factory = {}
        factoryTypes.factory["Repositories"] = constructorMock("Repositories")
        factoryTypes.factory["Issues"] = constructorMock("Issues")
        factoryTypes.factory["Wikis"] = constructorMock("Wikis")


    def testCreationOfStrategyOk(self):
        factoryType = factoryTypes.FactoryTypes()
        strategyR = factoryType.factory_method("Repositories")
        strategyI = factoryType.factory_method("Issues")
        strategyW = factoryType.factory_method("Wikis")
        self.assertEqual(strategyR.get_name(),"Repositories")
        self.assertEqual(strategyI.get_name(),"Issues")
        self.assertEqual(strategyW.get_name(),"Wikis")

    def testCreationOfStrategyWrong(self):
        factoryType = factoryTypes.FactoryTypes()
        strategyR = factoryType.factory_method("Asd")
        self.assertEqual(None,strategyR)

if __name__ == '__main__':
    unittest.main()
