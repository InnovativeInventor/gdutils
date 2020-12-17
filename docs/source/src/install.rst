Installation Guide
==================

To install the ``gdutils`` package, run the following ``pip3`` command:
::

    $ pip3 install git+https://github.com/mggg/gdutils.git


Manual Installation
-------------------

To manually install the ``gdutils`` package, clone the repository with the
following command:
::

    $ git clone https://github.com/mggg/gdutils.git

and install the dependecies and make a local ``gdutils`` build with
following commands:
::
    
    $ cd gdutils
    $ pip3 install --upgrade pip
    $ python3 setup.py bdist_wheel
    $ pip3 install dist/*.whl

Alternatively, if you have a \*nix OS or `gcc`, you can install dependencies and
a local build using ``make``. For example:
::

    $ cd gdutils
    $ make install
    $ make clean


Uninstallation
-------------------

To uninstall ``gdutils``, run ``pip3 uninstall gdutils``.
