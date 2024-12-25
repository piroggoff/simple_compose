import logging

# creating logger
logger = logging.getLogger('main_server')
logger.setLevel(logging.DEBUG)

# handlers definition
console_handler = logging.StreamHandler()
file_handler = logging.FileHandler('main_server.log')
console_handler.setLevel(logging.DEBUG)
file_handler.setLevel(logging.ERROR)

# formatting time
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
console_handler.setFormatter(formatter)
file_handler.setFormatter(formatter)

logger.addHandler(console_handler)
logger.addHandler(file_handler)

# Example log messages
# server_logger.debug('This is a debug message')
# logger.info('This is an info message')
# logger.warning('This is a warning message')
# logger.error('This is an error message')
# logger.critical('This is a critical message')
