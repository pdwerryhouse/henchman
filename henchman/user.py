
from henchman.rule import RuleType
from henchman import Henchman, rules

# This will be fixed when we have more than one provider
import henchman.provider.user.usermod as provider

import pwd
import os
import string

class UserType(RuleType):

    __named_attribute__ = 'name'

    def create(self):
        provider.create(self.params)

    def remove(self):
        provider.remove(self.params)

    def run(self):

        if self.params.get('ensure') in (None, "present"):
            if not provider.exists(self.params.get('name')):
                self.create()
            else:
                provider.sync(self.params)

        elif self.params.get('ensure') == 'absent':
            self.remove()

def User(name, **kwargs):
    rules.add(UserType(name,**kwargs))

def USER(name):
    return ("UserType", name)

