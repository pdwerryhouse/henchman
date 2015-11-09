
import grp
import os
import string

def exists(name):
    try:
        group = pwd.getgrnam(name)
    except KeyError:
        return False

    return True

def sync(params):

    gid = params.get('gid')

    options = []

    if gid != None: options.append("-g %s" % (gid))

    options_string = string.join(options," ")

    os.system("groupmod %s %s 2>/dev/null" % (options_string, params.get('name')))
    
def create(params):
    try:
        group = pwd.getpwnam(params.get('name'))
        return
    except KeyError as e:
        user = None
    
    gid = params.get('gid')

    options = []

    if gid != None: options.append("-g %s" % (gid))

    options_string = string.join(options," ")

    os.system("groupadd %s %s" % (options_string, params.get('name')))

def remove(params):
    if not exists(params.get('name')):
        return

    os.system("groupdel %s" % (params.get('name')))
