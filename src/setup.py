#!/usr/bin/python

from setuptools import setup, find_packages

setup(
    name   ='WorkingWithFiles',
    version='0.1.1',
    author='Fernando Pujaico Rivera',
    author_email='fernando.pujaico.rivera@gmail.com',
    packages=['WorkingWithFiles'],
    #scripts=['bin/script1','bin/script2'],
    url='https://github.com/trucomanx/WorkingWithFiles',
    license='GPLv3',
    description='functions to find and list files',
    #long_description=open('README.txt').read(),
    install_requires=[
       "natsort" #"Django >= 1.1.1",#
    ],
)

#! python setup.py sdist bdist_wheel
# Upload to PyPi
# or 
#! pip3 install dist/WorkingWithFiles-0.1.0.tar.gz 
