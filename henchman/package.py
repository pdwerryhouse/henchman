
from henchman.rule import Rule

class Package(Rule):

    __named_attribute__ = 'name'

    def operate(self):

        if self.params.get('ensure') in (None, "present", "installed"):
            pass

        elif self.params.get('ensure') == 'absent':
            pass

        elif self.params.get('ensure') == 'purged':
            pass

        elif self.params.get('ensure') == 'latest':
            pass

        elif self.params.get('ensure') == 'held':
            pass
