from distutils.core import setup
setup(
    name = 'matplotlib_venn_wordcloud',
    packages = ['matplotlib_venn_wordcloud'],
    version = '0.1',
    description = 'Create a Venn diagram with word clouds corresponding to each subset.',
    author = 'Paul Brodersen',
    author_email = 'paulbrodersen+matplotlib_venn_wordcloud@gmail.com',
    url = 'https://github.com/paulbrodersen/matplotlib_venn_wordcloud',
    download_url = 'https://github.com/paulbrodersen/matplotlib_venn_wordcloud/archive/0.1.tar.gz',
    keywords = ['matplotlib', 'venn', 'wordcloud'],
    classifiers = [ # Get strings from http://pypi.python.org/pypi?%3Aaction=list_classifiers
        'Development Status :: 4 - Beta',
        'Intended Audience :: Science/Research',
        'License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)'
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 3',
        'Topic :: Scientific/Engineering :: Visualization'
    ],
    platforms=['Platform Independent'],
    install_requires=['matplotlib', 'numpy', 'scipy', 'matplotlib-venn', 'wordcloud'],
)
