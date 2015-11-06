
from henchman.rule import RuleType
from henchman import Henchman, rules

import pwd
import os
import string

class UserType(RuleType):

    __named_attribute__ = 'name'

    def create(self):
        try:
            user = pwd.getpwnam(self.params.get('name'))
            return
        except KeyError as e:
            user = None
        
        uid = self.params.get('uid')
        gid = self.params.get('gid')
        comment = self.params.get('comment')
        shell = self.params.get('shell')

        options = []

        if uid != None: options.append("-u %s" % (uid))
        if gid != None: options.append("-g %s" % (gid))
        if comment != None: options.append("-c '%s'" % (comment))
        if shell != None: options.append("-c '%s'" % (shell))

        options_string = string.join(options," ")

        os.system("useradd %s %s" % (options_string, self.params.get('name')))

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

