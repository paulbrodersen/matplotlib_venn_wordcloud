#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Given 2 or 3 sets or words, create a Venn diagram
with word clouds corresponding to each subset.
"""

import numpy as np
import matplotlib.pyplot as plt
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

    wordcloud_kwargs: dict
        passed to wordcloud.WordCloud;
        some arguments are fixed, including
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
            Returns the circle patch corresponding to each idx (as in .id2idx).

    """

    # check input as requirements for "sets" differs from venn2 "subsets"
    assert np.all(type(elem) == set for elem in sets), "All elements of 'sets' arguments need to be sets!"
    assert len(sets) == 2, "Number of sets needs to be 2!"

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

    def _func(id):
        return [word for (word, word_id) in zip(words, word_ids) if word_id==id]
    venn.get_words_by_id = _func

    return _venn_wordcloud(venn, ax, wordcloud_kwargs)


def venn3_wordcloud(sets,
                    set_labels=None,
                    set_colors=['w', 'w', 'w'],
                    set_edgecolors=['k', 'k', 'k'],
                    alpha=0.8,
                    ax=None,
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

    wordcloud_kwargs: dict
        passed to wordcloud.WordCloud;
        some arguments are fixed, including
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
            Returns the circle patch corresponding to each idx (as in .id2idx).

    """

    # check input as requirements for "sets" differs from venn3 "subsets"
    assert np.all(type(elem) == set for elem in sets), "All elements of 'sets' arguments need to be sets!"
    assert len(sets) == 3, "Number of sets needs to be 3!"

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

    def _func(id):
        return [word for (word, word_id) in zip(words, word_ids) if word_id==id]
    venn.get_words_by_id = _func

    return _venn_wordcloud(venn, ax, wordcloud_kwargs)


def _venn_wordcloud(ExtendedVennDiagram, ax, wordcloud_kwargs):
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
        mpl_text.set_text('')

    # divide axis into pixels
    xlim = ax.get_xlim()
    ylim = ax.get_ylim()
    width = xlim[1] - xlim[0]
    height = ylim[1] - ylim[0]
    x_resolution = 1000
    y_resolution = int(height * x_resolution / width)
    x = np.linspace(xlim[0], xlim[1], x_resolution)
    y = np.linspace(ylim[0], ylim[1], y_resolution)
    xgrid, ygrid = np.meshgrid(x, y)
    pixels = np.c_[xgrid.ravel(), ygrid.ravel()]

    # create a word cloud for each patch region and combine word clouds into one image
    img_rgba = np.zeros((y_resolution, x_resolution, 4), dtype=np.float)
    for uid in ExtendedVennDiagram.uids:
        # get the boolean mask corresponding to each patch
        patch = ExtendedVennDiagram.get_patch_by_id(uid)
        path = patch.get_path()
        mask = path.contains_points(pixels).reshape((y_resolution, x_resolution))

        # make mask matplotlib-venn compatible
        mask = (~mask * 255).astype(np.uint8) # black indicates mask position
        mask = np.flipud(mask) # origin is in upper left

        # create wordcloud
        # wordcloud_kwargs.setdefault('color_func', _color_func)
        wc = WordCloud(mask=mask,
                       background_color=None,
                       mode="RGBA",
                       **wordcloud_kwargs)
        # text = " ".join(subset2words[uid])
        text = " ".join(ExtendedVennDiagram.get_words_by_id(uid))
        wc.generate(text)

        # add wordcloud to image
        img_rgba += wc.to_array()

    # matplotlib alpha values are between 0.-1.,
    # not 0-255 as returned by matplotlib-venn
    img_rgba /= 255.

    # plot word clouds on top of venn diagram
    subax = _add_subplot_axes(ax, (0, 0, 1, 1))
    subax.imshow(img_rgba, interpolation='bilinear')
    subax.set_frame_on(False)
    subax.set_xticks([])
    subax.set_yticks([])

    return ExtendedVennDiagram


# TODO: eliminate dependency
def _add_subplot_axes(ax, rect, axisbg='w', axis_alpha=0.):
    fig = ax.get_figure()
    box = ax.get_position()
    width = box.width
    height = box.height
    inax_position  = ax.transAxes.transform(rect[0:2])
    transFigure = fig.transFigure.inverted()
    infig_position = transFigure.transform(inax_position)
    x = infig_position[0]
    y = infig_position[1]
    width *= rect[2]
    height *= rect[2]
    subax = fig.add_axes([x,y,width,height],axisbg=axisbg)
    x_labelsize = subax.get_xticklabels()[0].get_size()
    y_labelsize = subax.get_yticklabels()[0].get_size()
    x_labelsize *= rect[2]**0.5
    y_labelsize *= rect[3]**0.5
    subax.xaxis.set_tick_params(labelsize=x_labelsize)
    subax.yaxis.set_tick_params(labelsize=y_labelsize)
    subax.patch.set_alpha(axis_alpha)
    return subax
