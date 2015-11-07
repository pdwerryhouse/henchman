
import pwd
import os
import string

class Usermod(object):

    def create(self, **kwargs):
        try:
            user = pwd.getpwnam(kwargs.get('name'))
            return
        except KeyError as e:
            user = None
        
        uid = kwargs.get('uid')
        gid = kwargs.get('gid')
        comment = kwargs.get('comment')
        shell = kwargs.get('shell')

        options = []

        if uid != None: options.append("-u %s" % (uid))
        if gid != None: options.append("-g %s" % (gid))
        if comment != None: options.append("-c '%s'" % (comment))
        if shell != None: options.append("-s '%s'" % (shell))

        options_string = string.join(options," ")

        os.system("useradd %s %s" % (options_string, kwargs.get('name')))

    def remove(self, **kwargs):
        try:
            user = pwd.getpwnam(kwargs.get('name'))
        except KeyError as e:
            return

