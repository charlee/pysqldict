========
Overview
========

.. start-badges

.. list-table::
    :stub-columns: 1

    * - docs
      - |docs|
    * - tests
      - | |travis| |appveyor| |requires|
        |
    * - package
      - | |version| |wheel| |supported-versions| |supported-implementations|
        | |commits-since|
.. |docs| image:: https://readthedocs.org/projects/pysqldict/badge/?style=flat
    :target: https://readthedocs.org/projects/pysqldict
    :alt: Documentation Status

.. |travis| image:: https://travis-ci.org/charlee/pysqldict.svg?branch=master
    :alt: Travis-CI Build Status
    :target: https://travis-ci.org/charlee/pysqldict

.. |appveyor| image:: https://ci.appveyor.com/api/projects/status/github/charlee/pysqldict?branch=master&svg=true
    :alt: AppVeyor Build Status
    :target: https://ci.appveyor.com/project/charlee/pysqldict

.. |requires| image:: https://requires.io/github/charlee/pysqldict/requirements.svg?branch=master
    :alt: Requirements Status
    :target: https://requires.io/github/charlee/pysqldict/requirements/?branch=master

.. |version| image:: https://img.shields.io/pypi/v/pysqldict.svg
    :alt: PyPI Package latest release
    :target: https://pypi.org/project/pysqldict

.. |commits-since| image:: https://img.shields.io/github/commits-since/charlee/pysqldict/v0.1.0.svg
    :alt: Commits since latest release
    :target: https://github.com/charlee/pysqldict/compare/v0.1.0...master

.. |wheel| image:: https://img.shields.io/pypi/wheel/pysqldict.svg
    :alt: PyPI Wheel
    :target: https://pypi.org/project/pysqldict

.. |supported-versions| image:: https://img.shields.io/pypi/pyversions/pysqldict.svg
    :alt: Supported versions
    :target: https://pypi.org/project/pysqldict

.. |supported-implementations| image:: https://img.shields.io/pypi/implementation/pysqldict.svg
    :alt: Supported implementations
    :target: https://pypi.org/project/pysqldict


.. end-badges

A library that allows python dictionaries to be stored in SQLite and provides a simple interface for read and write.

* Free software: MIT license

Installation
============

::

    pip install pysqldict

Documentation
=============


https://pysqldict.readthedocs.io/


Development
===========

To run the all tests run::

    tox

Note, to combine the coverage data from all the tox environments run:

.. list-table::
    :widths: 10 90
    :stub-columns: 1

    - - Windows
      - ::

            set PYTEST_ADDOPTS=--cov-append
            tox

    - - Other
      - ::

            PYTEST_ADDOPTS=--cov-append tox
