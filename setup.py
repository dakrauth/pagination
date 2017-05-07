import os, sys
from setuptools import setup, find_packages

VERSION = __import__('pagination').get_version()
DESCRIPTION = 'Yet another update of django-pagination.'

setup(
    name='pagination',
    version=VERSION,
    url='https://github.com/dakrauth/pagination',
    author_email='dakrauth@gmail.com',
    description=DESCRIPTION,
    long_description=DESCRIPTION,
    author='David A Krauth',
    platforms=['any'],
    license='BSD License',
    classifiers=[
        'Environment :: Web Environment',
        'Framework :: Django',
        'License :: OSI Approved :: BSD License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3.5',
    ],
    packages=find_packages(),
    package_data={'pagination': ['pagination/*']}
)
