
import os

def enable(params):
    name = params.get('name')
    override = "/etc/init/%s.override" % (name,)
    if os.path.exists(override):
        os.unlink(override)

def disable(params):
    name = params.get('name')
    override = "/etc/init/%s.override" % (name,)
    f=open(override,'w')
    f.write("manual\n")
    f.close()
