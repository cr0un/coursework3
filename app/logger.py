import logging

def my_logger():

    logger = logging.getLogger("basic")
    logger.setLevel("DEBUG")

    file_handler = logging.FileHandler("log.txt")
    logger.addHandler(file_handler)

    formatter = logging.Formatter("%(asctime)s [%(levelname)s] %(message)s")
    file_handler.setFormatter(formatter)

    return logger