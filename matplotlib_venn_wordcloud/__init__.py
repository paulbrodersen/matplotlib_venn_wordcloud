#!/usr/bin/env python
# -*- coding: utf-8 -*-

# matplotlib_venn_wordcloud.py --- Create a Venn diagram with word clouds corresponding to each subset.

# Copyright (C) 2017 Paul Brodersen <paulbrodersen+matplotlib_venn_wordcloud@gmail.com>

# Author: Paul Brodersen <paulbrodersen+matplotlib_venn_wordcloud@gmail.com>

# Permission is hereby granted, free of charge, to any person obtaining a
# copy of this software and associated documentation files (the "Software"),
# to deal in the Software without restriction, including without limitation
# the rights to use, copy, modify, merge, publish, distribute, sublicense,
# and/or sell copies of the Software, and to permit persons to whom the
# Software is furnished to do so, subject to the following conditions:

# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.

# Except as contained in this notice, the name(s) of the above copyright
# holders shall not be used in advertising or otherwise to promote the sale,
# use or other dealings in this Software without prior written authorization.

# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.  IN NO EVENT SHALL
# THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING
# FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER
# DEALINGS IN THE SOFTWARE.

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
__version__ = '0.2.1'
