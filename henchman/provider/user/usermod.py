
import pwd
import os
import string

class Usermod(object):

    @staticmethod
    def create(params):
        try:
            user = pwd.getpwnam(params.get('name'))
            return
        except KeyError as e:
            user = None
        
        uid = params.get('uid')
        gid = params.get('gid')
        comment = params.get('comment')
        shell = params.get('shell')

        options = []

        if uid != None: options.append("-u %s" % (uid))
        if gid != None: options.append("-g %s" % (gid))
        if comment != None: options.append("-c '%s'" % (comment))
        if shell != None: options.append("-s '%s'" % (shell))

        options_string = string.join(options," ")

        os.system("useradd %s %s" % (options_string, params.get('name')))

    @staticmethod
    def remove(params):
        try:
            user = pwd.getpwnam(params.get('name'))
        except KeyError as e:
            return

