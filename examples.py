#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""

"""

import venn_wordcloud; reload(venn_wordcloud)

def ex1():

    test_string_1 = "Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam nonumy eirmod tempor invidunt ut labore et dolore magna aliquyam erat, sed diam voluptua."

    test_string_2 = " At vero eos et accusam et justo duo dolores et ea rebum. Stet clita kasd gubergren, no sea takimata sanctus est Lorem ipsum dolor sit amet."

    sets = []

    for string in [test_string_1, test_string_2]:
        # convert to all lower case
        string = string.lower()

        # get a word list
        words = string.split(' ')

        # remove non alphanumeric characters
        words = [''.join(ch for ch in word if ch.isalnum()) for word in words]

        sets.append(set(words))

    venn_wordcloud.venn2_wordcloud(sets)

    return

def ex2():
    """
    Answer to
    http://stackoverflow.com/questions/43059781/connecting-networks-by-adding-edge-between-same-items-in-the-networks
    """

    HH = ['GLI1', 'PTCH1', 'PTCH2', 'WNT5A', 'HHIP1', 'MYCN', 'CCND1', 'CCND2', 'BCL2', 'CFLAR', 'FOXF1', 'FOXL1', 'PRDM1', 'JAG2', 'GREM1']
    Wnt = ['GLI1', 'PTCH1', 'WNT5A', 'HHIP1', 'MYCN', 'CCND1', 'WNT7A', 'WNT2', 'CDK1', 'CK1']
    CC = ['GLI1', 'CCNDA', 'BMP4', 'BMP7', 'MTOC2', 'CCND1']

    venn_wordcloud.venn3_wordcloud([set(HH), set(Wnt), set(CC)],
                                   set_labels=['Hedgehog', 'Wnt', 'Cell Cycle'])

    return

def _ex3():

    for string in [test_string_1, test_string_2]:

        # get a word list
        words = string.split(' ')

        # remove non alphanumeric characters
        words = [''.join(ch for ch in word if ch.isalnum()) for word in words]

        # TODO: tokenize words
        # TODO: also probably want to remove common words like "the" and "and"

        # count occurrences; remove duplicates
        from collections import Counter
        counter = Counter()
        for word in words:
            counter[word] += 1
        words, counts = counter.keys(), np.array(counter.values())

        # convert counts to reasonable fontsizes
        max_fontsize = 25
        max_count = np.float(np.max(counts))
        fontsizes = counts / max_count * max_fontsize

    return
