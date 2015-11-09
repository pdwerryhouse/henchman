
import pwd
import os
import string

def exists(name):
    try:
        user = pwd.getpwnam(name)
    except KeyError:
        return False

    return True

def sync(params):

    uid = params.get('uid')
    gid = params.get('gid')
    comment = params.get('comment')
    shell = params.get('shell')
    home = params.get('home')

    options = []

    if uid != None: options.append("-u %s" % (uid))
    if gid != None: options.append("-g %s" % (gid))
    if comment != None: options.append("-c '%s'" % (comment))
    if shell != None: options.append("-s '%s'" % (shell))
    if home != None: options.append("-d '%s'" % (home))

    options_string = string.join(options," ")

    os.system("usermod %s %s 2>/dev/null" % (options_string, params.get('name')))
    
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
    home = params.get('home')

    options = []

    if uid != None: options.append("-u %s" % (uid))
    if gid != None: options.append("-g %s" % (gid))
    if comment != None: options.append("-c '%s'" % (comment))
    if shell != None: options.append("-s '%s'" % (shell))
    if home != None: options.append("-d '%s'" % (home))

    options_string = string.join(options," ")

    os.system("useradd %s %s" % (options_string, params.get('name')))

def remove(params):
    if not exists(params.get('name')):
        return

    os.system("usermod %s" % (params.get('name')))
