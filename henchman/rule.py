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

class RuleType(object):

    def __init__(self, name, **kwargs):

        self.rulename = (self.__class__.__name__, name)
        self.params = kwargs
        if self.params.get(self.__named_attribute__) == None:
            self.params[self.__named_attribute__] = name

    def get_rulename(self):
        return self.rulename

    def get_refname(self):
        (x,y) = self.rulename
        return "%s('%s')" % (self.__refname__, y)

    def __str__(self):
        (x, y) = self.rulename
        return "[ %s: %s ]" % (x,y)

    def go(self):
        if self.completed == True:  return
        self.completed = True
        self.run()

    def run(self):
        pass
