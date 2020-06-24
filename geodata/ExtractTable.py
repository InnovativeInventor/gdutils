__doc__ = '''
ExtractTable
============

Provides
    1. A python class used to extract tabular data by column and value. 
       Can manage filetypes: csv, xlsx, geojson, shp
    2. Table pivoting (if `VALUE` is not specified)
    3. A command-line script to run the class' extract function

Metadata
--------
filename:       ExtractTable.py
author:         @KeiferC
date:           23 June 2020
version:        0.0.1
description:    Script to extract tabular data by column to a CSV
dependencies:   geopandas
                matplotlib
                maup
                numpy
                pandas

Documentation
-------------
Documentation for the ExtractTable module can be found as docstrings in the
source code. Run `help(ExtractTable)` to view documentation.

Usage
-----
```
ExtractTable.py [-h] [-v VALUE] [-o OUTFILE] -c COLUMN INFILE

script to extract tabular data by column to a CSV

positional arguments:
    INFILE                path to file from which to extract data

optional arguments:
-h, --help            show this help message and exit
-v VALUE, --value VALUE
                        value to use as filter for extraction
-o OUTFILE, --output OUTFILE
                        path to output extracted table

required arguments:
-c COLUMN, --column COLUMN
                        column name with value to extract and to become new
                        index

examples:

    python ExtractTable.py input.xlsx -c ID > output.csv
    python ExtractTable.py foo.csv -o bar.csv -c "state fips" -v 01
    python Extract.py input.csv -o ../output.csv -c Name -v "Rick Astley"

```
'''

import argparse
import geopandas as gpd
import matplotlib.pyplot as plt
import maup
import numpy as np
import os.path
import pandas as pd
import sys
import zipfile

import warnings; warnings.filterwarnings(
    'ignore', 'GeoSeries.isna', UserWarning)



#########################################
# Class Definition                      #
#########################################
class ExtractTable:
    '''
    Class for extracting tabular data. Run `help(ExtractTable)` to view docs
    '''

    #--------------------------------
    # Constructors                  
    #--------------------------------
    def __init__(self, infile=None, outfile=None, column=None, value=None):
        self.__infile = None
        self.__outfile = None
        self.__column = None
        self.__value = None

        self.__table = None
        self.__coldata = None
        self.__extracted = None

        self.__sanitize_init(infile, outfile, column, value)


    @classmethod
    def read_file(self, filename, column=None, value=None):
        '''
        Returns an ExtractTable instance with a specified input filename

        Parameters
        ----------
        filename : str
            Input file to read
        column : str | None
            Label of column to use as index for extracted table
        value : str | None
            Value to use as filter for extracted table

        Returns
        -------
        ExtractTable
        '''

        return self(filename, None, column, val)
    

    # Constructor input sanitation
    def __sanitize_init(self, infile, outfile, column, value):
        try:
            self.infile = infile
            self.outfile = outfile
            self.column = column
            self.value = value
        except Exception as e:
            print("Initialization Error:", e)


    #--------------------------------
    # Getters and Setters                 
    #--------------------------------
    @property
    def infile(self):
        '''
        {str} 
            Path to tabular data file containing tables to extract
        '''
        return self.__infile

    @infile.setter
    def infile(self, filename):
        if filename:
            try:
                self.__table = gpd.read_file(filename)
                self.__infile = filename
            except Exception as e:
                print("File opening error:", e)


    @property
    def outfile(self):
        '''
        {str | None}
            Path to output csv file containing extracted table. 
            Defaults to stdout
        '''
        return self.__outfile

    @outfile.setter
    def outfile(self, filename=None):
        self.__outfile = filename


    @property
    def column(self):
        '''
        {str}
            Name of column in source table to use as index for extracted table
        '''
        return self.__column

    @column.setter
    def column(self, column):
        if column:
            try:
                self.__coldata = self.__table[column]
                self.__column = column
            except Exception as e:
                print('Column not found error:', e)


    @property
    def value(self):
        '''
        {str | None}
            Value in column in source table to use as filter for extracting 
            subtable. If not specified, output file is a rotated table
        '''
        return self.__value

    @value.setter
    def value(self, value):
        if value:
            try:
                self.__extracted = self.__table.loc[
                                        self.__table[self.column] == value]
                if self.__extracted.empty:
                    raise Exception('column "{}" has no value "{}"'.format(
                                        self.column, value))
                else:
                    self.__value = value
            except Exception as e:
                print('Value not found error:', e)


    #--------------------------------
    # Method Definitions                
    #--------------------------------
    def __pivot(self):
        return self.__extracted # TODO

    def extract(self):
        return self.__pivot()


    def to_file(self):
        pass # TODO


#########################################
# Command-Line Parsing                  #
#########################################
def parse_arguments():
    '''
    Parses command-line arguments and returns a dictionary of argument objects

    Parameters
    ----------
    None

    Returns
    -------
    An argparse Namespace object
    '''

    description = 'script to extract tabular data by column as a CSV'
    infile_help = 'path to file from which to extract data'
    column_help = 'column label to use as extracted index'
    value_help = 'value in column to use as filter for extraction'
    outfile_help = 'path to output extracted table'
    
    examples = \
'''
examples:
    
    python ExtractTable.py input.xlsx -c ID > output.csv
    python ExtractTable.py foo.csv -o bar.csv -c "state fips" -v 01
    python ExtractTable.py input.csv -o ../output.csv -c Name -v "Rick Astley"
    
'''

    parser = argparse.ArgumentParser(
                description=description,
                epilog=examples,
                formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument(
                'infile',
                metavar='INFILE', 
                help=infile_help)
    parser.add_argument(
            '-v', 
            '--value', 
            dest='value',
            metavar='VALUE', 
            type=str, 
            help=value_help)
    parser.add_argument(
            '-o', 
            '--output', 
            dest='outfile',
            metavar='OUTFILE', 
            type=str, 
            help=outfile_help)
    
    required = parser.add_argument_group('required arguments')
    required.add_argument(
                '-c', 
                '--column', 
                dest='column', 
                metavar='COLUMN', 
                type=str, 
                required=True,
                help=column_help)

    return parser.parse_args()


#########################################
# Main                                  #
#########################################
def main():
    '''
    Validates input, parses command-line arguments, runs program.

    Parameters
    ----------
    None

    Returns
    -------
    None
    '''

    args = parse_arguments()

    # TODO

    sys.exit()


#########################################
# Regression Tests                      #
#########################################
def run_tests():
    et = ExtractTable()
    print(et.infile)
    et.infile = "test/test1.csv"
    print(et.infile)
    et.infile = "test/asdf"
    print(et.infile)
    et.column = "col1"
    print(et.column)
    et.value = "c"
    extracted = et.extract()
    print(type(extracted))
    print(extracted.head())


#########################################
# Function Calls                        #
#########################################
if __name__ == "__main__":
        #main()
        run_tests()



