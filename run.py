"""Running the Xetra ETL application"""
import logging
import logging.config

import yaml

def main():
    """
        entry point to run the xetra ETL job
    """
    # Parsing YAML file
    config_path = 'C:/Jingyi/xetra_project/xetra_experiment/configs/xetra_report1_config.yml'
    config = yaml.safe_load(open(config_path))
    # configurate logging - use the logging session in the yaml file
    log_config = config['logging']
    # load log_config (our file) as a dictionary to configurate our logging
    logging.config.dictConfig(log_config)
    # use the name of our file ('__main__'/run.py) as our root logger
    # it is a common practice to create a logger using the name of the file
    logger =logging.getLogger(__name__)
    # Xetra Transformer - 2022-06-21 16:47:40,911 - INFO - This is a test.
    # logger.info("This is a test.")


if __name__ == '__main__':
    main()