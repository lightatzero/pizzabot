#!/usr/bin/env python

from setuptools import setup

setup(name='pizzabot',
    version='0.1.0',
    author='light at zero',
    author_email='lightatzero@gmail.com',
    packages=['pizzabot'],
    install_requires=[
        "coordinates",
        "pytest",
    ],
    scripts=['bin/pizzabot'],
)
