

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

rules = Henchman()
