
import sys
from configurator import Configurator
from connector import Connector
from resulting import Result
from testProcessor import TestProcessor

def run():
#tesing of commit to Git
#    config = Configurator(sys.argv[1])
    config = Configurator("dev")
    database_url = config.get_database_url()

    connector = Connector(database_url)

    logger = Result()

    test_processor = TestProcessor(config, connector, logger)
    test_processor.process()

    logger.finish_test()


if __name__ == '__main__':
    run()
