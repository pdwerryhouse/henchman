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

