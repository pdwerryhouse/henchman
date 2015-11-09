
import networkx as nx
import matplotlib.pyplot as plt

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
            self.rules[i].run()

rules = Henchman()
