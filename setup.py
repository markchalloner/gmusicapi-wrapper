#!/usr/bin/env python2
# -*- coding: utf-8 -*-

import re
import sys
from setuptools import find_packages, setup

if not ((2, 7, 0) <= sys.version_info[:3] < (2, 8)):
	sys.exit("gmusicapi-wrapper only supports Python 2.7.")

# From http://stackoverflow.com/a/7071358/1231454
version_file = "gmusicapi_wrapper/__init__.py"
version_re = r"^__version__ = ['\"]([^'\"]*)['\"]"

version_file_contents = open(version_file).read()
match = re.search(version_re, version_file_contents, re.M)

if match:
	version = match.group(1)
else:
	raise RuntimeError("Could not find version in '%s'" % version_file)

setup(
	name='gmusicapi-wrapper',
	version=version,
	description='A wrapper interface around gmusicapi.',
	license='MIT',
	author='thebigmunch',
	author_email='mail@thebigmunch.me',
	url='https://github.com/thebigmunch/gmusicapi-wrapper',
	keywords=[],
	classifiers=[
		'License :: OSI Approved :: MIT License',
		'Programming Language :: Python :: 2',
		'Programming Language :: Python :: 2.6',
		'Programming Language :: Python :: 2.7',
	],
	packages=find_packages(),
	install_requires=[
		'gmusicapi',
		'mutagen'
	],
	zip_safe=False
)
