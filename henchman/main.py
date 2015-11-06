

class Henchman(object):

    def __init__(self):
        self.rules = {}
        self.queue = []

    def add(self, rule):
        name = rule.get_rulename()
        self.rules[name] = rule

    def list(self):
        for k,v in self.rules.iteritems():
            print k,v 

    def get(self, ruletype, name):
        return self.rules[(ruletype, name)]

    def calculate_dependencies(self):
        for k,v in self.rules.iteritems():
            if v.params.get("require") == None:
                self.queue.insert(0,k)
            else:
                self.queue.append(k)

    def run(self):
        for i in self.queue:
            self.rules[i].operate()


rules = Henchman()
