#!/usr/bin/env python
# -*- coding: utf-8 -*-

# matplotlib_venn_wordcloud.py --- Create a Venn diagram with word clouds corresponding to each subset.

# Copyright (C) 2016 Paul Brodersen <paulbrodersen+matplotlib_venn_wordcloud@gmail.com>

# Author: Paul Brodersen <paulbrodersen+matplotlib_venn_wordcloud@gmail.com>

# This program is free software; you can redistribute it and/or
# modify it under the terms of the GNU General Public License
# as published by the Free Software Foundation; either version 3
# of the License, or (at your option) any later version.

# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.

# You should have received a copy of the GNU General Public License
# along with this program. If not, see <http://www.gnu.org/licenses/>.

"""
Matplotlib Venn Wordcloud
=========================

Create a Venn diagram with word clouds corresponding to each subset.

Example:
--------

import venn_wordcloud

test_string_1 = "Lorem ipsum dolor sit amet, consetetur sadipscing
elitr, sed diam nonumy eirmod tempor invidunt ut labore et dolore
magna aliquyam erat, sed diam voluptua."

test_string_2 = "At vero eos et accusam et justo duo dolores et ea
rebum. Stet clita kasd gubergren, no sea takimata sanctus est Lorem
ipsum dolor sit amet."

sets = []

# tokenize words (approximately at least):
for string in [test_string_1, test_string_2]:
    # get a word list
    words = string.split(' ')

    # remove non alphanumeric characters
    words = [''.join(ch for ch in word if ch.isalnum()) for word in words]

    # convert to all lower case
    words = [word.lower() for word in words]

    sets.append(set(words))

# create visualisation
venn_wordcloud.venn2_wordcloud(sets)

"""

from matplotlib_venn_wordcloud._main import venn2_wordcloud, venn3_wordcloud
__all__ = ['venn2_wordcloud', 'venn3_wordcloud']
__version__ = '0.1'
