import logging
import logging.handlers as handlers

from ocr.ocr_image.Config import config


# not used, remove it later
def get_logger(name):
    logger = logging.getLogger(name)
    if config.log_type == 'DEBUG':
        logger.setLevel(logging.DEBUG)
    else:
        logger.setLevel(logging.INFO)

    # Here we define our formatter
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

    log_handler = handlers.TimedRotatingFileHandler(config.log_dir + '/normal.log',
                                                    when='D', interval=1, backupCount=0)
    log_handler.setLevel(logging.INFO)
    log_handler.setFormatter(formatter)

    error_log_handler = handlers.RotatingFileHandler(config.log_dir + '/error.log', maxBytes=5000, backupCount=10)
    error_log_handler.setLevel(logging.ERROR)
    error_log_handler.setFormatter(formatter)

    logger.addHandler(log_handler)
    logger.addHandler(error_log_handler)

    return logger
