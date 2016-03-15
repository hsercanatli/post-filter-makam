#!/usr/bin/env python

from setuptools import setup

setup(name='pitchfilter',
    version='1.1-tomato',
    description='Post filtering on pitch tracks',
    author='Hasan Sercan Atli',
    url='https://github.com/hsercanatli/pitch-post-filter',
    packages=['pitchfilter'], 
    install_requires=[
      "numpy",
    ],
)
