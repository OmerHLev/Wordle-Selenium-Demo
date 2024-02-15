import inspect
import logging


class LoggerClass:
    def __init__(self):
        logger_name = inspect.stack()[1][3]
        logger = logging.getLogger(logger_name)
        if len(logger.handlers) == 0:
            filehandler = logging.FileHandler('logfile.log')
            formatter = logging.Formatter("%(asctime)s: %(levelname)s: %(funcName)s: %(message)s")
            filehandler.setFormatter(formatter)
            logger.addHandler(filehandler)
        logger.setLevel(logging.DEBUG)
        logger.propagate = False
        self.logger_object = logger
