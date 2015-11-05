
from henchman.rule import RuleType
from henchman import Henchman, rules

class PackageType(RuleType):

    __named_attribute__ = 'name'

    def operate(self):

        if self.params.get('ensure') in (None, "present", "installed"):
            pass

        elif self.params.get('ensure') == 'absent':
            pass

        elif self.params.get('ensure') == 'purged':
            pass

        elif self.params.get('ensure') == 'latest':
            pass

        elif self.params.get('ensure') == 'held':
            pass

def Package(name, **kwargs):
    rules.add(PackageType(name,**kwargs))

def PACKAGE(name):
    return rules.get("PackageType", name)
