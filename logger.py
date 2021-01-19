from logging.handlers import TimedRotatingFileHandler
import logging
import sys


FORMATTER = logging.Formatter(
    '%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    datefmt='%m/%d/%Y %H:%M:%S')
LOG_FILE = "thoughtsmanager.log"


def get_logger():
    logger = logging.getLogger(__name__)
    logger.setLevel(logging.DEBUG)
    logger.addHandler(console_handler())
    logger.addHandler(file_handler())
    logger.propagate = False
    return logger


def console_handler():
    console_handler = logging.StreamHandler(sys.stdout)
    console_handler.setFormatter(FORMATTER)
    console_handler.setLevel(logging.INFO)
    return console_handler


def file_handler():
    file_handler = TimedRotatingFileHandler(LOG_FILE,
                                            when='midnight')
    file_handler.setFormatter(FORMATTER)
    file_handler.setLevel(logging.DEBUG)
    return file_handler


def smtp_handler():
    pass
