from setuptools import setup, find_packages
from codecs import open
from os import path

"""
Copyright (C) 2016: Jennifer Helsby
"""

here = path.abspath(path.dirname(__file__))

with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='crosscorr',

    # Versions should comply with PEP440
    version='1.0',
    description='Computing to generate redshifts by cross-correlation',
    long_description=long_description,
    url='https://github.com/redshiftzero/crosscorr',
    author='Jennifer Helsby',
    author_email='jen@redshiftzero.com',
    license='GPL v3',
    classifiers=[
        'Development Status :: 2 - Alpha',
        'Intended Audience :: Science/Research',
        'Topic :: Scientific/Engineering :: Astronomy', 
        'Topic :: Scientific/Engineering :: Physics', 
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Natural Language :: English',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7'
    ],

    keywords='astronomy astrophysics cosmology redshifts galaxies',

    packages=find_packages(exclude=['images', 'docs', 'tests*']),

    setup_requires=['numpy', 'scipy'],
    install_requires=['numpy', 'pyyaml', 'pandas', 'esutil',
                      'datetime', 'scipy',
                      'fitsio', 'matplotlib'],

    # Dev package requirements
    # $ pip install -e .[dev,test]
    extras_require={
        'dev': ['nose'],
        'test': ['nose'],
    },

    package_data={
        'sample': ['default.yaml']
    },

    test_suite='nose.collector',
    tests_require=['nose']

)
