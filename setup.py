# -*- coding: utf-8 -*-
import os
from setuptools import setup


# allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

setup(
    name='django-themes',
    version='0.1',
    packages=['themes'],
    include_package_data=True,
    license='BSD License',  # example license
    description='Simple css classes generator',
    long_description="",
    url='http://www.codesgroup.eu/',
    author='Timofei Mihhailov',
    author_email='timofeimih@gmail.com.com',
    classifiers=[
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License', # example license
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        # Replace these appropriately if you are stuck on Python 2.
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
    ],
)
