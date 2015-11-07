
from henchman.rule import RuleType
from henchman import Henchman, rules
import henchman.provider.user.usermod

import pwd
import os
import string

class UserType(RuleType):

    __named_attribute__ = 'name'

    def create(self):
        henchman.provider.user.usermod.Usermod.create(self.params)

    def remove(self):
        henchman.provider.user.usermod.Usermod.remove(self.params)

    def run(self):

        if self.params.get('ensure') in (None, "present"):
            self.create()

        elif self.params.get('ensure') == 'absent':
            self.remove()

def User(name, **kwargs):
    rules.add(UserType(name,**kwargs))

def USER(name):
    return rules.get("UserType", name)

