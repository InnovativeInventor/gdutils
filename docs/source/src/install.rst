Installation Guide
==================

To install ``gdutils`` package, run the following ``pip3`` command:
::

    $ conda install fiona shapely pyproj rtree && pip3 install wheel
    $ pip3 install git+https://github.com/mggg/gdutils.git


Manual Installation
-------------------

To manually install ``gdutils`` package, clone the repository with the
following command:
::

    $ git clone https://github.com/mggg/gdutils.git

To install the dependecies and a local ``gdutils`` build, run the
following commands:
::
    
    $ cd gdutils
    $ conda install fiona shapely pyproj rtree
    $ pip3 install --upgrade pip
    $ python3 setup.py bdist_wheel
    $ pip3 install dist/*.whl

Alternatively, if you have a \*nix OS, you can install dependencies and
a local build using ``make``. 

If you only wish to use the ``gdutils`` module in a specific project directory,
clone the ``gdutils`` repository into your project directory and install 
dependencies running ``pip3 install -r requirements.txt`` inside the cloned
directory.
