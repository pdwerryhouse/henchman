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

import apt

class PackageType(RuleType):

    __named_attribute__ = 'name'
    __refname__ = 'PACKAGE'

    def install(self):
        cache = apt.Cache()
        pkg = cache[self.params.get('name')]
        pkg.mark_install()
        cache.commit()
        pass

    def uninstall(self):
        cache = apt.Cache()
        pkg = cache[self.params.get('name')]
        pkg.mark_delete()
        cache.commit()
        pass

    def run(self):

        if self.params.get('ensure') in (None, "present", "installed"):
            self.install()

        elif self.params.get('ensure') == 'absent':
            self.uninstall()

        elif self.params.get('ensure') == 'purged':
            self.uninstall()

        elif self.params.get('ensure') == 'latest':
            pass

        elif self.params.get('ensure') == 'held':
            pass

def Package(name, **kwargs):
    rules.add(PackageType(name,**kwargs))

def PACKAGE(name):
    return ("PackageType", name)
