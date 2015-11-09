
from henchman.rule import RuleType
from henchman import Henchman, rules
import re
import string

blank = re.compile('[ \t]*$')
comment = re.compile('[ \t]*#')

def parse_hosts(hostfile):
    hosts = {}
    f = open(hostfile, "r")
    for line in f.readlines():
        line = line.rstrip()
        if blank.match(line) or comment.match(line):
            continue
        items = re.split('[ \t]+',line)
        host = {}
        host['ipaddr'] = items[0]
        host['name'] = items[1]
        host['aliases'] = []
        for i in items[2:]:
            host['aliases'].append(i)
        hosts[items[0] + '#' + items[1]] = host 

    return hosts

def write_hosts(hosts, hostfile):
    
    f = open(hostfile, 'w')

    for k,v in hosts.iteritems():
        f.write("%s %s %s\n" % (v['ipaddr'], v['name'], string.join(v['aliases'])))

    f.close()

class HostType(RuleType):

    __named_attribute__ = 'name'
    __refname__ = 'HOST'

    def run(self):

        hosts = parse_hosts('/var/tmp/hosts')

        if self.params.get('ensure') in (None, "present"):
            name = self.params.get('name')
            host_aliases = self.params.get('host_aliases')
            ip = self.params.get('ip')
            host = {}
            host['name'] = name
            host['ipaddr'] = ip
            host['aliases'] = host_aliases or ''

            hosts[ip + '#' + name] = host

        elif self.params.get('ensure') == 'absent':
            pass

        write_hosts(hosts, '/var/tmp/hosts')

def Host(name, **kwargs):
    rules.add(HostType(name,**kwargs))

def HOST(name):
    return ("HostType", name)

