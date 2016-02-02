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
