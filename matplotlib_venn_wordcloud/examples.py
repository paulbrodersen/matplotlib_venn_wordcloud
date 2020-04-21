#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Example use cases.
"""
import numpy as np
import matplotlib.pyplot as plt

from matplotlib_venn_wordcloud import venn2_wordcloud, venn3_wordcloud


def ex1():
    """
    Minimal example.
    """

    test_string_1 = "Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam nonumy eirmod tempor invidunt ut labore et dolore magna aliquyam erat, sed diam voluptua."

    test_string_2 = "At vero eos et accusam et justo duo dolores et ea rebum. Stet clita kasd gubergren, no sea takimata sanctus est Lorem ipsum dolor sit amet."

    # tokenize words (approximately at least):
    sets = []
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


def ex2():
    """
    Answer to
    http://stackoverflow.com/questions/43059781/connecting-networks-by-adding-edge-between-same-items-in-the-networks
    """

    HH = ['GLI1', 'PTCH1', 'PTCH2', 'WNT5A', 'HHIP1', 'MYCN', 'CCND1', 'CCND2', 'BCL2', 'CFLAR', 'FOXF1', 'FOXL1', 'PRDM1', 'JAG2', 'GREM1']
    Wnt = ['GLI1', 'PTCH1', 'WNT5A', 'HHIP1', 'MYCN', 'CCND1', 'WNT7A', 'WNT2', 'CDK1', 'CK1']
    CC = ['GLI1', 'CCNDA', 'BMP4', 'BMP7', 'MTOC2', 'CCND1']

    venn3_wordcloud([set(HH), set(Wnt), set(CC)],
                    set_labels=['Hedgehog', 'Wnt', 'Cell Cycle'])

    return


def ex3():
    """
    Answer to
    http://stackoverflow.com/questions/42812083/auto-venn-diagram-text-rendering/42839350#42839350
    """

    just_dem = ["sincerely", "women", "service", "newsletter", "program", "families",
                "community", "funding", "important", "million", "department"]
    dem_and_rep = ["country", "make", "support", "state", "people", "jobs", "American",
                   "care", "health", "president", "work", "veterans", "tax", "survey",
                   "years", "need", "economy"]
    just_rep = ["security", "nation", "Obama", "energy", "law", "spending",
                "budget", "states", "committee", "passed", "job", "business"]
    dem = just_dem + dem_and_rep
    rep = just_rep + dem_and_rep

    def color_func(word, *args, **kwargs):
        if word in just_dem:
            # return "#000080" # navy blue
            return "#0000ff" # blue1
        elif word in just_rep:
            # return "#8b0000" # red4
            return "#ff0000" # red1
        else:
            return "#0f0f0f" # gray6 (aka off-black)

    words = just_dem + dem_and_rep + just_rep

    # for testing, assign random word frequencies;
    # frequencies = np.random.rand(len(words))
    # frequencies /= np.sum(frequencies)

    # word frequencies follow Zipf's law;
    # words will probably be within the 10k most frequent words;
    # however, we will probably exclude the 1000 most common words from analysis;
    frequencies = 1. / np.arange(1000, 10000) # Zipf's law with alpha = 1
    frequencies = np.random.choice(frequencies, size=len(words))

    word_to_frequency = dict(zip(words, frequencies))

    fig, ax = plt.subplots(1,1)
    ax.set_title("Congress says what?", fontsize=36)
    venn2_wordcloud([set(dem), set(rep)],
                    set_labels=["Democrats", "Republicans"],
                    set_edgecolors=['b', 'r'],
                    word_to_frequency=word_to_frequency,
                    wordcloud_kwargs=dict(color_func=color_func, relative_scaling=.5),
                    ax=ax)


def ex4():
    """
    Issue #2:
    https://github.com/paulbrodersen/matplotlib_venn_wordcloud/issues/2
    """

    from matplotlib import pyplot as plt
    from matplotlib_venn_wordcloud import venn2_wordcloud

    x = {'sincerely','department', 'usa', 'usa nation'}
    y = {'sincerely','security','usa democracy'}
    s = (x,y)

    v = venn2_wordcloud(s)


def ex5():
    """
    Issue #4:
    https://github.com/paulbrodersen/matplotlib_venn_wordcloud/issues/4

    Handle non-overlapping sets gracefully.
    """
    from matplotlib import pyplot as plt
    from matplotlib_venn_wordcloud import venn2_wordcloud

    x = set('abcd')
    y = set('efgh')
    s2 = (x,y)

    v2 = venn2_wordcloud(s2)

    z = set('ijkl')
    s3 = (x, y, z)
    v3 = venn3_wordcloud(s3)


def ex6():
    """
    Issue #5:
    https://github.com/paulbrodersen/matplotlib_venn_wordcloud/issues/5

    Allow user to specify max_font_size/min_font_size.
    """

    test_string_1 = "Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam nonumy eirmod tempor invidunt ut labore et dolore magna aliquyam erat, sed diam voluptua."

    test_string_2 = "At vero eos et accusam et justo duo dolores et ea rebum. Stet clita kasd gubergren, no sea takimata sanctus est Lorem ipsum dolor sit amet."

    # tokenize words (approximately at least):
    sets = []
    for string in [test_string_1, test_string_2]:

        # get a word list
        words = string.split(' ')

        # remove non alphanumeric characters
        words = [''.join(ch for ch in word if ch.isalnum()) for word in words]

        # convert to all lower case
        words = [word.lower() for word in words]

        sets.append(set(words))

    # create visualisation
    fig, axes = plt.subplots(2, 2, figsize=(20, 20))
    ax2, ax3, ax4, ax5 = axes.ravel()

    # These paramater values hould have no effect as the given min and
    # max font size should be much larger than WC would want them to
    # be anyway (negative control).
    venn2_wordcloud(sets, wordcloud_kwargs=dict(max_font_size=1000, min_font_size=0), ax=ax2)
    ax2.set_title('max_font_size and min_font_size outside range')

    # Positive controls
    venn2_wordcloud(sets, wordcloud_kwargs=dict(max_font_size=50), ax=ax3)
    ax3.set_title('max_font_size=50')

    venn2_wordcloud(sets, wordcloud_kwargs=dict(min_font_size=30), ax=ax4)
    ax4.set_title('min_font_size=30')

    venn2_wordcloud(sets, wordcloud_kwargs=dict(max_font_size=50, min_font_size=30), ax=ax5)
    ax5.set_title('max_font_size=50, min_font_size=30')


if __name__ == "__main__":

    ex1()
    ex2()
    ex3()
    ex4()
    ex5()
    ex6()

    plt.show()
