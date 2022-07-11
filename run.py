"""Running the Xetra ETL application"""
import argparse
import logging
import logging.config

import yaml

from xetra.common.s3 import S3BucketConnector
from xetra.transformers.xetra_transformer import XetraETL, XetraSourceConfig, XetraTargetConfig

def main():
    """
        entry point to run the xetra ETL job
    """
    # Parsing YAML file
    parser = argparse.ArgumentParser(description='Run the Xetra ETL job.')
    parser.add_argument('config', help='Directory of a configuration file in yaml format.') 
    args = parser.parse_args()
    # config_path = 'C:/Jingyi/xetra_project/xetra_experiment/configs/xetra_report1_config.yml'
    config = yaml.safe_load(open(args.config))

    # configurate logging - use the logging session in the yaml file
    log_config = config['logging']
    # load log_config (our file) as a dictionary to configurate our logging
    logging.config.dictConfig(log_config)
    # use the name of our file ('__main__'/run.py) as our root logger
    # it is a common practice to create a logger using the name of the file
    logger =logging.getLogger(__name__)
    # Xetra Transformer - 2022-06-21 16:47:40,911 - INFO - This is a test.
    logger.info("This is a test.")

    # reading s3 configuration
    s3_config = config['s3']
    # creating the S3BucketConnector class instances for source and target 
    s3_bucket_src = S3BucketConnector(access_key=s3_config['access_key'],
                                        secret_key=s3_config['secret_key'],
                                        endpoint_url=s3_config['src_endpoint_url'],
                                        bucket=s3_config['src_bucket'])
    s3_bucket_trg = S3BucketConnector(access_key=s3_config['access_key'],
                                        secret_key=s3_config['secret_key'],
                                        endpoint_url=s3_config['trg_endpoint_url'],
                                        bucket=s3_config['trg_bucket'])

    # reading source configuration
    source_config = XetraSourceConfig(**config['source'])
    # reading target configuration
    target_config = XetraTargetConfig(**config['target'])
    # reading meta file configuration
    meta_config = config['meta']
    # creating XetraETL class instance
    logger.info('Xetra ETL job started.')
    xetra_etl = XetraETL(s3_bucket_src, s3_bucket_trg, meta_config['meta_key'], source_config, target_config)
    # running etl job for xetra report1
    xetra_etl.etl_report1()
    logger.info('Xetra ETL job finished.')


if __name__ == '__main__':
    main()