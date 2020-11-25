from setuptools import setup

install_dependencies = [
      'numpy == 1.*',
      'pandas == 1.*',
      'geopandas == 0.*'
]

test_dependencies = [
      'pytest'
]

setup(name='gdutils',
      version='1.0.0',
      description='A collection of geodata tools',
      url='https://github.com/KeiferC/gdutils',
      author='@KeiferC',
      license='MIT', 
      packages=['gdutils'],
      install_requires=install_dependencies,
      tests_requires=test_dependencies,
      test_suite='pytest')
