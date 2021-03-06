#!/usr/bin/env python
"""
DNS Zone File
==============

"""

from setuptools import setup, find_packages

setup(
    name='blockstack-zones',
    version='0.1.6',
    url='https://github.com/blockstack/dns-zone-file-py',
    license='MIT',
    author='Blockstack Developers',
    author_email='hello@onename.com',
    description=("Library for creating and parsing DNS zone files"),
    keywords='dns zone file zonefile parse create',
    packages=find_packages(),
    zip_safe=False,
    install_requires=[
        'future'
    ],
    classifiers=[
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Internet',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ]
)
