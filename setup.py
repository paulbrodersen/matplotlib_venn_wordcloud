from setuptools import setup, find_packages
setup(
    name = 'matplotlib_venn_wordcloud',
    version = '0.2.1',
    description = 'Create a Venn diagram with word clouds corresponding to each subset.',
    author = 'Paul Brodersen',
    author_email = 'paulbrodersen+matplotlib_venn_wordcloud@gmail.com',
    url = 'https://github.com/paulbrodersen/matplotlib_venn_wordcloud',
    download_url = 'https://github.com/paulbrodersen/matplotlib_venn_wordcloud/archive/0.2.1.tar.gz',
    keywords = ['matplotlib', 'venn', 'wordcloud'],
    classifiers = [ # Get strings from http://pypi.python.org/pypi?%3Aaction=list_classifiers
        'Development Status :: 4 - Beta',
        'Intended Audience :: Science/Research',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 3',
        'Topic :: Scientific/Engineering :: Visualization'
    ],
    platforms=['Platform Independent'],
    packages=find_packages(),
    install_requires=['numpy', 'matplotlib', 'matplotlib-venn', 'wordcloud'],
)
