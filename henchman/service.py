
from henchman.rule import RuleType
from henchman import Henchman, rules

import henchman.provider.service.upstart

import os.path

class ServiceType(RuleType):

    __named_attribute__ = 'name'
    __refname__ = 'SERVICE'

    def run(self):

        provider = None
        name = self.params.get('name')

        if os.path.exists('/bin/systemctl'):
            provider = henchman.provider.service.systemctl
        
        elif os.path.exists('/etc/init/%s.conf' % (name,)):
            provider = henchman.provider.service.upstart

        else:
            provider = henchman.provider.service.debian

        if self.params.get('enable') == "true":
            provider.enable(self.params)

        elif self.params.get('enable') == 'false':
            provider.disable(self.params)

def Service(name, **kwargs):
    rules.add(ServiceType(name,**kwargs))

def SERVICE(name):
    return ("ServiceType", name)

