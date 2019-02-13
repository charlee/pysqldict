# Overview

+-----------------------------------+-----------------------------------+
| docs                              | [![Documentation Status](https:// |
|                                   | readthedocs.org/projects/pysqldic |
|                                   | t/badge/?style=flat)](https://rea |
|                                   | dthedocs.org/projects/pysqldict)  |
+-----------------------------------+-----------------------------------+
| tests                             | | [![Travis-CI Build Status](http |
|                                   | s://travis-ci.org/charlee/pysqldi |
|                                   | ct.svg?branch=master)](https://tr |
|                                   | avis-ci.org/charlee/pysqldict)    |
|                                   |   [![AppVeyor Build Status](https |
|                                   | ://ci.appveyor.com/api/projects/s |
|                                   | tatus/github/charlee/pysqldict?br |
|                                   | anch=master&svg=true)](https://ci |
|                                   | .appveyor.com/project/charlee/pys |
|                                   | qldict)                           |
|                                   |   [![Requirements Status](https:/ |
|                                   | /requires.io/github/charlee/pysql |
|                                   | dict/requirements.svg?branch=mast |
|                                   | er)](https://requires.io/github/c |
|                                   | harlee/pysqldict/requirements/?br |
|                                   | anch=master)                      |
|                                   | |                                 |
+-----------------------------------+-----------------------------------+
| package                           | | [![PyPI Package latest release] |
|                                   | (https://img.shields.io/pypi/v/py |
|                                   | sqldict.svg)](https://pypi.org/pr |
|                                   | oject/pysqldict)                  |
|                                   |   [![PyPI Wheel](https://img.shie |
|                                   | lds.io/pypi/wheel/pysqldict.svg)] |
|                                   | (https://pypi.org/project/pysqldi |
|                                   | ct)                               |
|                                   |   [![Supported versions](https:// |
|                                   | img.shields.io/pypi/pyversions/py |
|                                   | sqldict.svg)](https://pypi.org/pr |
|                                   | oject/pysqldict)                  |
|                                   |   [![Supported implementations](h |
|                                   | ttps://img.shields.io/pypi/implem |
|                                   | entation/pysqldict.svg)](https:// |
|                                   | pypi.org/project/pysqldict)       |
|                                   | | [![Commits since latest release |
|                                   | ](https://img.shields.io/github/c |
|                                   | ommits-since/charlee/pysqldict/v0 |
|                                   | .1.0.svg)](https://github.com/cha |
|                                   | rlee/pysqldict/compare/v0.1.0...m |
|                                   | aster)                            |
+-----------------------------------+-----------------------------------+

A library that allows python dictionaries to be stored in SQLite and
provides a simple interface for read and write.

- Free software: MIT license

## Installation

    pip install pysqldict

## Documentation

https://pysqldict.readthedocs.io/

## Development

To run the all tests run:

    tox

Note, to combine the coverage data from all the tox environments run:

+------+---------------------------------------------------------------+
| Wind |     set PYTEST_ADDOPTS=--cov-append                           |
| ows  |     tox                                                       |
+------+---------------------------------------------------------------+
| Othe |     PYTEST_ADDOPTS=--cov-append tox                           |
| r    |                                                               |
+------+---------------------------------------------------------------+
