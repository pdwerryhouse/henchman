
from henchman.rule import RuleType

class HostType(RuleType):

    __named_attribute__ = 'name'

    def operate(self):

        if self.params.get('ensure') in (None, "present"):
            pass

        elif self.params.get('ensure') == 'absent':
            pass

def Host(name, **kwargs):
    rules.add(HostType(name,**kwargs))

def HOST(name):
    return rules.get("HostType", name)

