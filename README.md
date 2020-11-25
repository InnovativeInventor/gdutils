# gdutils
[![Documentation Status](https://readthedocs.org/projects/gdutils/badge/?version=latest)](https://gdutils.readthedocs.io/en/latest/?badge=latest)

A collection of geodata utility tools.

Available modules:

- `gdutils.datamine`: a `python` module for mining and listing data sources.
- `gdutils.dataqa`: a `python` module for comparing analyzing and comparing 
   data for QA purposes.
- `gdutils.extract`: a script and `python` module for extracting tabular 
   data for data science (data wrangling) purposes. A user-friendly, lite 
   wrapper of `geopandas` with the power of `pandas`.

## Requirements
- Python3
- pip3
- conda

## Installation
```bash
$ conda install fiona shapely pyproj rtree
$ pip install git+https://github.com/mggg/gdutils.git
```

To uninstall, run `pip uninstall gdutils`.

## Documentation
Documentation can be found on [Read the Docs](https://gdutils.readthedocs.io/).
Additionally, documentation for modules can be found using the `python` 
`help()` function, e.g. `import gdutils.datamine; help(gdutils.datamine)`.



