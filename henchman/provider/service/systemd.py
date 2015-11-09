
import os

def enable(params):
    name = params.get('name')
    os.system('/bin/systemctl enable %s.service' % (name,))

def disable(params):
    name = params.get('name')
    os.system('/bin/systemctl disable %s.service' % (name,))
