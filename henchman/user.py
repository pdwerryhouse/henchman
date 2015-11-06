
from henchman.rule import RuleType

class UserType(RuleType):

    __named_attribute__ = 'name'

    def operate(self):

        if self.params.get('ensure') in (None, "present"):
            pass

        elif self.params.get('ensure') == 'absent':
            pass

def User(name, **kwargs):
    rules.add(UserType(name,**kwargs))

def USER(name):
    return rules.get("UserType", name)

