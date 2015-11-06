
from henchman.rule import RuleType
from henchman import Henchman, rules

import apt

class PackageType(RuleType):

    __named_attribute__ = 'name'

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
    return rules.get("PackageType", name)
