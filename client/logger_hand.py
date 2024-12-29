import logging

# creating logger
logger = logging.getLogger('client-app')
logger.setLevel(logging.DEBUG)

# handlers definition
console_handler = logging.StreamHandler()
file_handler = logging.FileHandler('./client.log')
console_handler.setLevel(logging.info)
file_handler.setLevel(logging.ERROR)

# formatting time
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
console_handler.setFormatter(formatter)
file_handler.setFormatter(formatter)

logger.addHandler(console_handler)
logger.addHandler(file_handler)


