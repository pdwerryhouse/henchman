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

import networkx as nx

class Henchman(object):

    def __init__(self):
        self.rules = {}

    def add(self, rule):
        name = rule.get_rulename()
        self.rules[name] = rule

    def list(self):
        for k,v in self.rules.iteritems():
            print k,v 

    def get(self, ruletype, name):
        return self.rules[(ruletype, name)]

    def run(self):
        self.G = nx.DiGraph()
        for k,v in self.rules.iteritems():
            self.G.add_node(k)
            if v.params.get("require") != None:
                self.G.add_edge(v.params.get("require"),k)

        for i in nx.topological_sort(self.G):
            print "Executing %s." % self.rules[i].get_refname()
            self.rules[i].run()

rules = Henchman()
