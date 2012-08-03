#!/usr/bin/python
from setuptools import setup
setup(	name='dl',
	version='0.1',
	description='dl - rm with forgivness',
	author='Dan Brooks',
	author_email='dan@cs.uml.edu',
	url='http://www.github.com/allohakdan/dl.git',
#	packages=['dl'],
	scripts=['dl'],
	long_description="""\
	dl - rm with forgivness
	""",
	classifiers=[
		"License :: OSI Approved :: BSD License",
		"Programming Language :: Python",
		"Environment :: Console",
		"Development Status :: 4 - Beta",
		"Intended Audience :: Developers",
		"Operating System :: POSIX",
		"Topic :: Utilities"
	],
	keywords='dl, rm, archiving',
	license='BSD',
	install_requires=['argparse'],
	)
