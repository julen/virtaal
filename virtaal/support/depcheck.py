#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Copyright 2009-2010 Zuza Software Foundation
# Copyright 2013 F Wolff
#
# This file is part of Virtaal.
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, see <http://www.gnu.org/licenses/>.

__all__ = ['check_dependencies', 'extra_tests', 'import_checks']


# Modules to try and import:
import_checks = ['translate', 'gtk', 'lxml.etree', 'json', 'pycurl', 'sqlite3', 'wsgiref']


#########################
# Specific Module Tests #
#########################
MIN_GTK_VERSION = (2, 18, 0)
def test_gtk_version():
    try:
        import gtk
        return gtk.ver >= MIN_GTK_VERSION
        # GtkBuilder was in GTK+ earlier already, but at least this bug is
        # quite nasty:
        # https://bugzilla.gnome.org/show_bug.cgi?id=582025
        # That seems to be fixed in time for 2.18 which was released in
        # September 2009
    except Exception:
        pass
    return False

def test_sqlite3_version():
    try:
        #TODO: work out if we need certain versions
        try:
            from sqlite3 import dbapi2
        except ImportError:
            from pysqlite2 import dbapi2
        return True
    except Exception:
        pass
    return False

def test_json():
    # We can work with simplejson or json (available since Python 2.6)
    try:
        try:
            import simplejson as json
        except ImportError:
            import json
        return True
    except Exception:
        pass
    return False

MIN_TRANSLATE_VERSION = (1, 9, 0)
def test_translate_toolkit_version():
    try:
        from translate.__version__ import ver
        return ver >= MIN_TRANSLATE_VERSION
    except Exception:
        pass
    return False


extra_tests = {
    'gtk': test_gtk_version,
    'sqlite3': test_sqlite3_version,
    'translate': test_translate_toolkit_version,
    'json': test_json,
}


#############################
# General Testing Functions #
#############################
def test_import(modname):
    try:
        __import__(modname, {}, {}, [])
    except ImportError:
        return False
    return True

def check_dependencies(module_names=import_checks):
    """Returns a list of modules that could not be imported."""
    names = []
    for name in module_names:
        if name in extra_tests:
            if not extra_tests[name]():
                names.append(name)
        elif not test_import(name):
            names.append(name)
    return names



########
# MAIN #
########
if __name__ == '__main__':
    failed = check_dependencies()
    if not failed:
        print 'All dependencies met.'
    else:
        print 'Dependencies not met: %s' % (', '.join(failed))
