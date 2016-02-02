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

import os
import os.path

class FileType(RuleType):

    __named_attribute__ = 'path'
    __refname__ = "FILE"

    def mode(self, path):
        if self.params.get('mode') != None:
            os.chmod(path, self.params.get('mode'))

    def owner(self, path):
        if self.params.get('owner') != None:
            os.chown(path, self.params.get('owner'), -1)

    def group(self, path):
        if self.params.get('group') != None:
            os.chgrp(path, self.params.get('group'))

    def directory(self):
        path = self.params.get('path')

        if not os.path.exists(path):
            os.mkdir(path)

        if not os.path.isdir(path):
            os.unlink(path)
            os.mkdir(path)

        self.owner(path)
        self.group(path)
        self.mode(path)

    def file(self):
        path = self.params.get('path')

        f = open(path, "w")
        f.write(self.params.get('contents'))
        f.close()

        self.owner(path)
        self.group(path)
        self.mode(path)

    def absent(self):
        path = self.params.get('path')
        if not os.path.exists(path):
            return 

        if os.path.isdir(path):
            os.rmdir(path)

        elif os.path.isfile(path) or os.path.islink(path):
            os.unlink(path)

    def link(self):
        # XXX
        pass

    def run(self):

        if self.params.get('ensure') in (None, "file"):
            self.file()

        elif self.params.get('ensure') == 'directory':
            self.directory()

        elif self.params.get('ensure') == 'link':
            self.link()

        elif self.params.get('ensure') == 'absent':
            self.absent()

        elif self.params.get('ensure') == 'present':
            self.present()

def File(name, **kwargs):
    rules.add(FileType(name,**kwargs))

def FILE(name):
    return ("FileType", name)
