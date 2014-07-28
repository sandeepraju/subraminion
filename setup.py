# -*- coding: utf-8 -*-
# Copyright (c) 2014 Sandeep Raju. See LICENSE.txt for details.
from setuptools import setup

setup(
    name='Subraminion',
    version='0.0.3a',
    url='https://github.com/sandeepraju/subraminion',
    author='Sandeep Raju',
    author_email='me@sandeepraju.in',
    license=open('LICENSE.txt').read(),
    description='A nifty console tool to find / delete duplicate files.',
    long_description=open('README.md').read(),
    packages=['subraminion'],
    py_modules=['runner'],
    install_requires=[
    ],
    entry_points="""
    [console_scripts]
    subraminion=runner:run
    """
    )
