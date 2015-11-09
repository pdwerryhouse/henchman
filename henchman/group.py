
from henchman.rule import RuleType
from henchman import Henchman, rules

import henchman.provider.group.groupmod as provider

class GroupType(RuleType):

    __named_attribute__ = 'name'
    __refname__ = 'GROUP'

    def run(self):

        if self.params.get('ensure') in (None, "present"):
            if not provider.exists(self.params.get('name')):
                provider.create(self.params)
            else:
                provider.sync(self.params)

        elif self.params.get('ensure') == 'absent':
            provider.remove(self.params)

def Group(name, **kwargs):
    rules.add(GroupType(name,**kwargs))

def GROUP(name):
    return ("GroupType", name)

