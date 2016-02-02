#    Henchman: automation library
#    Copyright (C) 2016 Paul Dwerryhouse <paul@dwerryhouse.com.au>
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.

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

