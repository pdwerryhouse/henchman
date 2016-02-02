#    Henchman: automation library
#    Copyright (C) 2016 Paul Dwerryhouse <paul@dwerryhouse.com.au>
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.

from henchman.rule import RuleType
from henchman import Henchman, rules

import henchman.provider.service.upstart
import henchman.provider.service.systemd
import henchman.provider.service.debian

import os.path

class ServiceType(RuleType):

    __named_attribute__ = 'name'
    __refname__ = 'SERVICE'

    def run(self):

        provider = None
        name = self.params.get('name')

        if os.path.exists('/bin/systemctl'):
            provider = henchman.provider.service.systemd
        
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

