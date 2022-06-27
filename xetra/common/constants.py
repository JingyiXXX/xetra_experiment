"""
File to store constants
"""

from enum import Enum

class S3FileTypes(Enum):
    """
    supported file types for S3BucketConnector
    """

    # no __init__ here, these class attributes can be used immediately without
    # creating an instance.
    CSV = 'csv'
    PARQUET = 'parquet'


class MetaProcessFormat(Enum):
    """
    format for MetaProcess class
    """

    META_DATE_FORMAT = '%Y-%m-%d'
    META_PROCESS_DATE_FORMAT = '%Y-%m-%d %H:%M:%S'
    META_SOURCE_DATE_COL = 'source_date'
    META_PROCESS_COL = 'datetime_of_processing'
    META_FILE_FORMAT = 'csv'
