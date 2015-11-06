
from henchman.rule import RuleType
from henchman import Henchman, rules

import pwd
import os

class UserType(RuleType):

    __named_attribute__ = 'name'

    def create(self):
        try:
            user = pwd.getpwnam(self.params.get('name'))
        except KeyError as e:
            user = None
        
    def remove(self):
        try:
            user = pwd.getpwnam(self.params.get('name'))
        except KeyError as e:
            return

        os.system("userdel %s" % (self.params.get('name')))

    def run(self):

        if self.params.get('ensure') in (None, "present"):
            self.create()

        elif self.params.get('ensure') == 'absent':
            self.remove()

def User(name, **kwargs):
    rules.add(UserType(name,**kwargs))

def USER(name):
    return rules.get("UserType", name)

