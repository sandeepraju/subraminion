# -*- coding: utf-8 -*-
# Copyright (c) 2014 Sandeep Raju. See LICENSE.txt for details.
from setuptools import setup

setup(
    name='Subraminion',
    version='0.0.1-alpha',
    url='https://github.com/sandeepraju/subraminion',
    author='Sandeep Raju',
    author_email='me@sandeepraju.in',
    license=open('LICENSE.txt').read(),
    description='',
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