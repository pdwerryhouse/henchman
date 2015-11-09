
import os

def enable(params):
    name = params.get('name')
    os.system("/usr/sbin/update-rc.d %s enable" % (name,)

def disable(params):
    name = params.get('name')
    os.system("/usr/sbin/update-rc.d %s disable" % (name,)
