from setuptools import setup

install_dependencies = [
      "attrs           == 20.*",
      "certifi         == 2020.*",
      "chardet         == 4.*",
      "click           == 7.*",
      "click-plugins   == 1.*",
      "cligj           == 0.*",
      "Fiona           == 1.*",
      "geopandas       == 0.*",
      "idna            == 2.*",
      "iniconfig       == 1.*",
      "munch           == 2.*",
      "numpy           == 1.*",
      "packaging       == 20.*",
      "pandas          == 1.*",
      "pip             == 20.*",
      "pluggy          == 0.*",
      "py              == 1.*",
      "pyparsing       == 2.*",
      "pyproj          == 3.*",
      "pytest          == 6.*",
      "python-dateutil == 2.*",
      "pytz            == 2020.*",
      "requests        == 2.*",
      "setuptools      == 49.*",
      "Shapely         == 1.*",
      "six             == 1.*",
      "toml            == 0.*",
      "urllib3         == 1.*",
      "wheel           == 0.*"
]

test_dependencies = [
      'pytest'
]

setup(name='gdutils',
      version='1.1.1',
      description='A collection of geodata tools',
      url='https://github.com/KeiferC/gdutils',
      author='@KeiferC',
      license='MIT', 
      packages=['gdutils'],
      install_requires=install_dependencies,
      tests_requires=test_dependencies,
      test_suite='pytest')
