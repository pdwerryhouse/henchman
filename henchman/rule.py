
class RuleType(object):

    def __init__(self, name, **kwargs):

        self.rulename = (self.__class__.__name__, name)
        self.params = kwargs
        if self.params.get(self.__named_attribute__) == None:
            self.params[self.__named_attribute__] = name

    def get_rulename(self):
        return self.rulename

    def __str__(self):
        (x, y) = self.rulename
        return "[ %s: %s ]" % (x,y)

    def go(self):
        if self.completed == True:  return
        self.completed = True
        self.run()

    def run(self):
        pass
