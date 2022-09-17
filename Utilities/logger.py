import logging


def get_logger():
    """Define logger"""
    LOGGING_LEVEL = logging.DEBUG
    logger = logging.getLogger()
    logger.setLevel(LOGGING_LEVEL)
    ch = logging.StreamHandler()  # For terminal logging
    ch.setLevel(LOGGING_LEVEL)
    formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
    ch.setFormatter(formatter)
    logger.addHandler(ch)
    return logger
