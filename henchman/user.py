
from henchman.rule import RuleType
from henchman import Henchman, rules

# This will be fixed when we have more than one provider
import henchman.provider.user.usermod as provider

class UserType(RuleType):

    __named_attribute__ = 'name'
    __refname__ = 'USER'

    def run(self):

        if self.params.get('ensure') in (None, "present"):
            if not provider.exists(self.params.get('name')):
                provider.create(self.params)
            else:
                provider.sync(self.params)

        elif self.params.get('ensure') == 'absent':
            provider.remove(self.params)

def User(name, **kwargs):
    rules.add(UserType(name,**kwargs))

def USER(name):
    return ("UserType", name)

