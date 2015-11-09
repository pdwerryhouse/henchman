
from henchman.rule import RuleType
from henchman import Henchman, rules

class ServiceType(RuleType):

    __named_attribute__ = 'name'
    __refname__ = 'SERVICE'

    def run(self):

        if self.params.get('ensure') in (None, "present"):
            pass

        elif self.params.get('ensure') == 'absent':
            pass

def Service(name, **kwargs):
    rules.add(ServiceType(name,**kwargs))

def SERVICE(name):
    return ("ServiceType", name)

