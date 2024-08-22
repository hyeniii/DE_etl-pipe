"""Running the ETL application"""
import logging
import logging.config
import yaml

def main():
    """
    entry point to run ETL job
    """
    # Parse YAML file
    config_path = 'configs/etl_report_v1_config.yml'
    config = yaml.safe_load(open(config_path))
    # configure logging
    log_config = config['logging']
    logging.config.dictConfig(log_config)
    logger = logging.getLogger(__name__)
    logger.info("This is a test")


if __name__ == '__main__':
    main()