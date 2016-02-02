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

import grp
import os
import string

def exists(name):
    try:
        group = grp.getgrnam(name)
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
        group = grp.getgrnam(params.get('name'))
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
