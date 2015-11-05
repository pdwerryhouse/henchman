
from henchman.rule import Rule
import os
import os.path

class File(Rule):

    __named_attribute__ = 'path'

    #def __init__(self):
    #    super(File, self).__init__()

    def mode(self, path):
        if self.params.get('mode') != None:
            os.chmod(path, self.params.get('mode'))

    def owner(self, path):
        if self.params.get('owner') != None:
            os.chown(path, self.params.get('owner'))

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

    def operate(self):

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
