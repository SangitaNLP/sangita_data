#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: djokester
Samriddhi Sinha,
IIT Kharagpur
"""

import sys
from setuptools import setup

if sys.argv[-1] == 'setup.py':
    print('To install, run \'python setup.py install\'')
    print()

if sys.version_info[:2] < (3, 5):
    print(('lingatagger requires Python version 3.5 or later (%d.%d detected).' %sys.version_info[:2]))
    sys.exit(-1)

sys.path.insert(0, 'sangita_data')


if __name__ == "__main__":
    setup(
        name = "sangita_data",
        version = "1.0",
        author = "Samriddhi Sinha",
        author_email = "samridhhisinha.iitkgp@gmail.com",
        description = "Data and Corpus pertaining to Sangita",
        url='https://github.com/djokester/sangita_data',
        keywords= ['nlp', 'hindi', 'linguistics'],
        packages = ['sangita_data','sangita_data.hindi', 'sangita_data.hindi.sentences'],
        license = 'Apache License'
    )

