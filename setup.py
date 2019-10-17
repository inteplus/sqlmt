#!/usr/bin/env python3

from setuptools import setup, find_packages

setup(
    name='dataframemt',
    version='0.3.8',
    description="Extra Python modules to deal with dataframes for Minh-Tri Pham",
    author=["Minh-Tri Pham"],
    packages=find_packages(),
    install_requires=[
        'sqlalchemy',  # for psql access
        'pandas>=0.23.0',  # for dataframes
        'tzlocal',  # for getting the local timezone
        'psycopg2-binary',  # for psql access
        # 'mysql', # for mysql access
        'dask[dataframe]',  # for reading chunks of CSV files in parallel
        'basemt',  # Minh-Tri's base modules for logging and multi-threading
        # Minh-Tri modules for dealing with pandas.Series. Only for backward compatibility. Currently dataframemt does not require seriesmt.
        'seriesmt',
    ],
)
