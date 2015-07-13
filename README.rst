robotframework-psutil
====================

.. image:: https://travis-ci.org/guykisel/robotframework-psutil.svg?branch=master
    :target: https://pypi.python.org/pypi/robotframework-psutil
.. image:: https://pypip.in/v/robotframework-psutil/badge.png
    :target: https://pypi.python.org/pypi/robotframework-psutil
.. image:: https://pypip.in/d/robotframework-psutil/badge.png
    :target: https://pypi.python.org/pypi/robotframework-psutil
.. image:: https://pypip.in/license/robotframework-psutil/badge.png
    :target: https://pypi.python.org/pypi/robotframework-psutil

Robot Framework keyword library wrapper for
`psutil <https://github.com/giampaolo/psutil>`__.

This module allows easy use of psutil's system and process utilities.

Any docstrings psutil provides are passed through to Robot Framework, so
they're available in RIDE and in keyword documentation generated via
libdoc.

For more information on Robot Framework please visit `the Robot
Framework homepage! <http://robotframework.org/>`__

Installation
------------

``pip install robotframework-psutil``

Usage
-----

`PsutilLibrary keyword
documentation <https://guykisel.github.io/robotframework-psutil/>`__

.. code:: robotframework

    *** Settings ***
    Library    PsutilLibrary

    *** Test Cases ***
    PsutilLibrary CPU Count
        ${cpus}=    PsutilLibrary.Cpu Count
        Log    cpus: ${cpus}

See PsutilLibrary's tests for more usage examples.

Contribute
----------

If you like this module, please contribute! I welcome patches,
documentation, issues, ideas, and so on.


