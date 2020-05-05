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

from matplotlib_venn_wordcloud import venn2_wordcloud

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
venn2_wordcloud(sets)

"""

import numpy as np
import matplotlib.pyplot as plt

from matplotlib.patches import Circle
from wordcloud import WordCloud
from matplotlib_venn import venn2, venn3, venn2_circles, venn3_circles


def _default_color_func(*args, **kwargs):
    return '#00000f'


def venn2_wordcloud(sets,
                    set_labels=None,
                    set_colors=['w', 'w'],
                    set_edgecolors=['k', 'k'],
                    alpha=0.4,
                    ax=None,
                    word_to_frequency=None,
                    wordcloud_kwargs={'color_func':_default_color_func}):

    """
    Plot a Venn diagram based on two sets of words.
    The words are plotted as a word cloud on top.

    Arguments:
    ----------
    sets: [set_1, set_2]
        list of sets of words (or any strings)

    set_labels: [str_1, str_2]
        as in venn2

    set_colors: [str_1, str_2]
        as in venn2 (default: ['w', 'w'])
        face colour of each circle corresponding to each set;

    set_edgecolors: [str_1, str_2]
        edge colour of each circle corresponding to each set (default: ['b', 'b'])

    alpha: float
        face colour alpha value (default: 0.4)

    ax: matplotlib.axes._subplots.AxesSubplot instance or None
        axis to plot on

    word_to_frequency: dict or None (default: None)
        maps words to relative frequencies; used to scale word fontsizes

    wordcloud_kwargs: dict
        passed to wordcloud.WordCloud;
        some arguments are fixed, namely
            - background_color (None)
            - mode ("RGBA")
            - mask (computed based on subset patches)

    Returns:
    --------
    ExtendendVennDiagram:
        matplotlib_venn.VennDiagram instance
        with the addition of the following methods and attributes:

        .uids
            tuple of unique IDs
            venn2: ('10', '01', '11')
            venn3: ('100', '010', '110', '001', '101', '011', '111')

        .get_words_by_id(uid)
            Returns a list of words associated with each given subset.

        .get_circles_by_idx(idx)
            Returns the circle patch corresponding to each idx (idx as in .id2idx).

    """

    # check input as requirements for "sets" are more stringent than for venn2 "subsets"
    assert np.all(type(elem) == set for elem in sets), "All elements of 'sets' arguments need to be sets!"
    assert len(sets) == 2, "Number of sets needs to be 2!"
    assert np.all([len(s) > 0 for s in sets]), "All sets need to have at least one element!"

    # create venn diagram, grab ax
    if not ax:
        fig, ax = plt.subplots(1,1)

    venn = venn2(sets,
                 set_labels=set_labels,
                 set_colors=set_colors,
                 alpha=alpha,
                 ax=ax)

    # set edge color;
    # cannot use edgecolor attribute of patches returned by venn2
    # venn2 patches correspond to subsets and edges of patches are composed of several circles
    if set_edgecolors:
        venn_circles = venn2_circles(sets, ax=ax)
        for ii, patch in enumerate(venn_circles):
            patch.set_edgecolor(set_edgecolors[ii])
            patch.set_linewidth(3)

        # add circle handles to venn
        def _func(idx):
            return venn_circles[idx]

        venn.get_circle_by_idx = _func

    # make default set labels larger
    if set_labels:
        for label in venn.set_labels:
            label.set_fontsize(24.)

    # for each word compute its subset id
    words = list(set.union(*sets))
    word_ids = ['%d%d' % (word in sets[0], word in sets[1]) for word in words]

    # extend VennDiagram object
    venn.uids = set(word_ids)

    def _func(uid):
        return [word for (word, word_id) in zip(words, word_ids) if word_id==uid]

    venn.get_words_by_id = _func

    return _venn_wordcloud(venn, ax, word_to_frequency, **wordcloud_kwargs)


def venn3_wordcloud(sets,
                    set_labels=None,
                    set_colors=['w', 'w', 'w'],
                    set_edgecolors=['k', 'k', 'k'],
                    alpha=0.8,
                    ax=None,
                    word_to_frequency=None,
                    wordcloud_kwargs={'color_func':_default_color_func}):

    """
    Plot a Venn diagram based on two sets of words.
    The words are plotted as a word cloud on top.

    Arguments:
    ----------
    sets: [set_1, set_2, set_3]
        list of sets of words (or any strings)

    set_labels: [str_1, str_2, str_3]
        as in venn2

    set_colors: [str_1, str_2, str_3]
        as in venn2 (default: ['w', 'w'])
        face colour of each circle corresponding to each set;

    set_edgecolors: [str_1, str_2, str_3]
        edge colour of each circle corresponding to each set (default: ['b', 'b'])

    alpha: float
        face colour alpha value (default: 0.4)

    ax: matplotlib.axes._subplots.AxesSubplot instance or None
        axis to plot on

    word_to_frequency: dict or None (default: None)
        maps words to relative frequencies; used to scale word fontsizes

    wordcloud_kwargs: dict
        passed to wordcloud.WordCloud;
        some arguments are fixed, namely
            - background_color (None)
            - mode ("RGBA")
            - mask (computed based on subset patches)

    Returns:
    --------
    ExtendendVennDiagram:
        matplotlib_venn.VennDiagram instance
        with the addition of the following methods and attributes:

        .uids
            tuple of unique IDs
            venn2: ('10', '01', '11')
            venn3: ('100', '010', '110', '001', '101', '011', '111')

        .get_words_by_id(uid)
            Returns a list of words associated with each given subset.

        .get_circles_by_idx(idx)
            Returns the circle patch corresponding to each idx (idx as in .id2idx).

    """

    # check input as requirements for "sets" differs from venn3 "subsets"
    assert np.all(type(elem) == set for elem in sets), "All elements of 'sets' arguments need to be sets!"
    assert len(sets) == 3, "Number of sets needs to be 3!"
    assert np.all([len(s) > 0 for s in sets]), "All sets need to have at least one element!"

    # create venn diagram, grab ax
    if not ax:
        fig, ax = plt.subplots(1,1)

    venn = venn3(sets,
                 set_labels=set_labels,
                 set_colors=set_colors,
                 alpha=alpha,
                 ax=ax)

    # set edge color
    # cannot use edgecolor attribute of patches returned by venn2
    # venn2 patches correspond to subsets and edges of patches are composed of several circles
    if set_edgecolors:
        venn_circles = venn3_circles(sets, ax=ax)
        for ii, patch in enumerate(venn_circles):
            patch.set_edgecolor(set_edgecolors[ii])
            patch.set_linewidth(3)

        # add circle handles to venn
        def _func(idx):
            return venn_circles[idx]

        venn.get_circle_by_idx = _func

    # make default set labels larger
    if set_labels:
        for label in venn.set_labels:
            label.set_fontsize(24.)

    # for each word compute its subset id
    words = list(set.union(*sets))
    word_ids = ['%d%d%d' % (word in sets[0], word in sets[1], word in sets[2]) for word in words]

    # extend VennDiagram object
    venn.uids = set(word_ids)

    def _func(uid):
        return [word for (word, word_id) in zip(words, word_ids) if word_id==uid]

    venn.get_words_by_id = _func

    return _venn_wordcloud(venn, ax, word_to_frequency, **wordcloud_kwargs)


def _venn_wordcloud(ExtendedVennDiagram, ax, word_to_frequency=None, **wordcloud_kwargs):
    """
    Adds a wordcloud to an ExtendedVennDiagram.

    Arguments:
    ----------
    ExtendendVennDiagram:
        matplotlib_venn.VennDiagram instance
        with the addition of the following methods and attributes:

        .uids
            tuple of unique IDs
            venn2: ('10', '01', '11')
            venn3: ('100', '010', '110', '001', '101', '011', '111')

        .get_words_by_id(uid)
            Returns a list of words associated with each given subset.

    ax:
        matplotlib.axes._subplots.AxesSubplot instance

    Returns:
    --------
    ExtendedVennDiagram

    """

    # remove default subset labels; we will put a word cloud there instead
    for mpl_text in ExtendedVennDiagram.subset_labels:
        if mpl_text: # set intersection may not exist
            mpl_text.set_text('')

    # initialise an image that spans the axis
    img = _AxisImage(ax)

    # --------------------------------------------------------------------------------
    # Here be dragons!

    # The issue is that fontsizes need to be consistent (i.e. reflect
    # the overall word frequency) across the different patches
    # (subsets of the venn diagram). However, you can only figure out
    # the maximum/minimum fontsize for each patch by running the
    # packing algorithm. So you need to run wordcloud twice, first
    # without setting the maximum/minimum font size, then with setting
    # the maximum/minimum fontsize such that the relative word
    # frequencies appear consistent across patches.

    # figure out maximum fontsize for each set/wordcloud,
    # such that the fontsizes across sets/wordclouds are consistent with the relative frequencies
    # TODO: also take word bbox width into account
    given_max_font_size = wordcloud_kwargs.pop('max_font_size', None)
    given_min_font_size = wordcloud_kwargs.pop('min_font_size', None)

    max_font_sizes                 = np.full((len(ExtendedVennDiagram.uids)), np.nan)
    min_font_sizes                 = np.full_like(max_font_sizes, np.nan)
    max_font_size_word_frequencies = np.ones_like(max_font_sizes)
    min_font_size_word_frequencies = np.ones_like(max_font_sizes)
    # max_bbox_widths = np.zeros_like(max_font_sizes)
    for ii, uid in enumerate(ExtendedVennDiagram.uids):
        patch = ExtendedVennDiagram.get_patch_by_id(uid)
        words = ExtendedVennDiagram.get_words_by_id(uid)
        if (patch is None) and (len(words) > 0):
            msg = "Patch corresponding to subset {uid} does not exist even though the set appears to be non-empty:\n"
            for word in words:
                msg += '    {}\n'.format(word)
            msg += 'Skipping creation of wordcloud for subset {uid}'.format(uid=uid)
            import warnings
            warnings.warn(msg)
            continue

        wc = _get_wordcloud(img, patch, words, word_to_frequency, **wordcloud_kwargs)

        # bbox_widths = [len(item[0][0]) * item[1] for item in wc.layout_] # word, freq
        font_sizes = [item[1] for item in wc.layout_]
        max_idx = np.argmax(font_sizes)
        min_idx = np.argmin(font_sizes)
        max_font_sizes[ii] = font_sizes[max_idx]
        min_font_sizes[ii] = font_sizes[min_idx]

        if word_to_frequency:
            max_font_size_word = wc.layout_[max_idx][0][0]
            max_font_size_word_frequencies[ii] = word_to_frequency[max_font_size_word]
            min_font_size_word = wc.layout_[min_idx][0][0]
            min_font_size_word_frequencies[ii] = word_to_frequency[min_font_size_word]

    valid = ~np.isnan(max_font_sizes)
    max_font_sizes                 = max_font_sizes                [valid]
    min_font_sizes                 = min_font_sizes                [valid]
    max_font_size_word_frequencies = max_font_size_word_frequencies[valid]
    min_font_size_word_frequencies = min_font_size_word_frequencies[valid]

    idx = np.argmin(max_font_sizes / max_font_size_word_frequencies)
    max_font_sizes = max_font_size_word_frequencies * max_font_sizes[idx] / max_font_size_word_frequencies[idx]

    idx = np.argmin(min_font_sizes / min_font_size_word_frequencies)
    min_font_sizes = min_font_size_word_frequencies * min_font_sizes[idx] / min_font_size_word_frequencies[idx]

    # rescale min/max font sizes if a value is specified by the user
    if given_max_font_size:
        if given_max_font_size >= np.max(max_font_sizes):
            # Ignore the argument.
            # As is, we already don't have enough space for text objects of that
            # size in at least one of the patches.
            pass
        else:
            max_font_sizes *= given_max_font_size / np.max(max_font_sizes)

    if given_min_font_size:
        if given_min_font_size < np.min(min_font_sizes):
            # Ignore the argument. All minimum font sizes are larger.
            pass
        else:
            min_font_sizes *= given_min_font_size / np.min(min_font_sizes)

    # --------------------------------------------------------------------------------

    # create a word cloud for each patch region and combine word clouds into one image
    ctr = 0
    for ii, uid in enumerate(ExtendedVennDiagram.uids):
        patch = ExtendedVennDiagram.get_patch_by_id(uid)
        words = ExtendedVennDiagram.get_words_by_id(uid)
        if (patch is None):
            ctr += 1
            continue
        wc = _get_wordcloud(img, patch, words, word_to_frequency,
                            max_font_size=max_font_sizes[ii-ctr],
                            min_font_size=min_font_sizes[ii-ctr],
                            **wordcloud_kwargs)

        # matplotlib alpha values are between 0.-1.,
        # not 0-255 as returned by wordcloud
        img.rgba += wc.to_array() / 255.

    img.imshow(interpolation='bilinear')

    return ExtendedVennDiagram


def _get_wordcloud(img, patch, words, word_to_frequency=None, **wordcloud_kwargs):

    # get the boolean mask corresponding to each patch
    if isinstance(patch, Circle):
        # We need to solve two problems here:
        # 1) The path of Circle patches is always the unit circle.
        #    We need to apply the circle transform to the `path` attribute to get
        #    the correct path.
        # 2) The Circle object returned by matplotlib-venn is messed up.
        #    The transform is not doing what it should do.
        # path = transform.transform_path(old_path)

        # Create a new patch with the same parameters as the given Circle patch.
        dummy = Circle(patch.center, patch.radius)

        # Apply transform to get the correct path.
        transform = dummy.get_transform()
        unit_circle_path = dummy.get_path()
        path = transform.transform_path(unit_circle_path)
    else:
        path = patch.get_path()

    mask = path.contains_points(img.pixel_coordinates).reshape((img.y_resolution, img.x_resolution))

    # make mask matplotlib-venn compatible
    mask = (~mask * 255).astype(np.uint8) # black indicates mask position
    mask = np.flipud(mask) # origin is in upper left

    # create wordcloud
    wc = WordCloud(mask=mask,
                   background_color=None,
                   mode="RGBA",
                   **wordcloud_kwargs)

    if not word_to_frequency:
        # create mapping word : int
        word_to_frequency = dict()
        for word in words:
            try:
                word_to_frequency[word] += 1
            except KeyError:
                word_to_frequency[word] = 1

    wc.generate_from_frequencies({word: word_to_frequency[word] for word in words})

    return wc


class _AxisImage(object):
    """
    Create an image that spans the given axis.
    """

    def __init__(self, ax, resolution=1000):
        self.ax = ax
        self.x_resolution = resolution

        # set resolution in y
        xlim = ax.get_xlim()
        ylim = ax.get_ylim()
        width = xlim[1] - xlim[0]
        height = ylim[1] - ylim[0]
        self.y_resolution = int(height * self.x_resolution / width)

        # determine pixel coordinates
        x = np.linspace(xlim[0], xlim[1], self.x_resolution)
        y = np.linspace(ylim[0], ylim[1], self.y_resolution)
        xgrid, ygrid = np.meshgrid(x, y)
        self.pixel_coordinates = np.c_[xgrid.ravel(), ygrid.ravel()]

        # initialise pixel array
        self.rgba = np.zeros((self.y_resolution, self.x_resolution, 4), dtype=np.float)


    def imshow(self, **imshow_kwargs):
        # create a new axis on top of existing axis
        bbox = self.ax.get_position() # in figure coordinates
        fig = self.ax.get_figure()
        subax = fig.add_axes(bbox, facecolor=None)

        # plot image
        subax.imshow(self.rgba, **imshow_kwargs)

        # make pretty
        subax.set_frame_on(False)
        subax.set_xticks([])
        subax.set_yticks([])
