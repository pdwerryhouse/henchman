
from henchman.rule import Rule

class Host(Rule):

    __named_attribute__ = 'name'

    def operate(self):

        if self.params.get('ensure') in (None, "present"):
            pass

        elif self.params.get('ensure') == 'absent':
            pass
