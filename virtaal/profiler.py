#!/usr/bin/python
# -*- coding: utf-8 -*-
# 
# Copyright 2007 The authors of Jokosher
# Copyright 2008 Zuza Software Foundation
# 
# This file was part of Jokosher.
# This file is part of virtaal.
#
# virtaal is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2 of the License, or
# (at your option) any later version.
# 
# translate is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with translate; if not, write to the Free Software
# Foundation, Inc., 59 Temple Place, Suite 330, Boston, MA  02111-1307  USA

"""This module is meant for testing and profiling the code only. It should not 
be included in any release."""

import hotshot
from hotshot import stats

import main_window
prog = main_window.VirTaal()

profile = hotshot.Profile("Virtaal.profile", lineevents=1)
profile.runcall(prog.run)

s = stats.load("Virtaal.profile")

s.strip_dirs()
s.sort_stats("cumulative", "calls").print_stats()
s.sort_stats("time", "calls").print_stats()

