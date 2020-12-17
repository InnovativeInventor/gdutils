Installation Guide
==================

To install the ``gdutils`` package, run the following ``pip3`` command:
::

    $ pip3 install git+https://github.com/mggg/gdutils.git


Manual/Local Installation
-------------------------

To manually install the ``gdutils`` package, clone the repository and set
up a virtual environment with the following commands:
::

    $ git clone https://github.com/mggg/gdutils.git
    $ cd gdutils
    $ python3 -m venv venv
    $ source venv/bin/activate
    
and install the dependecies and make a local ``gdutils`` build with
following commands:
::
    
    $ pip3 install --upgrade pip
    $ python3 setup.py bdist_wheel
    $ pip3 install dist/*.whl

Alternatively, if you have a \*nix OS or ``gcc``, you can install dependencies 
and make a local build using ``make``. For example:
::

    $ make install
    $ make clean


Uninstallation
-------------------

To uninstall ``gdutils``, run ``pip3 uninstall gdutils``.
