import logging

logger = logging.getLogger('pi-block-explorer')
logger.setLevel(logging.INFO)

formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

file_handler = logging.FileHandler('pi-block-explorer.log')
file_handler.setFormatter(formatter)

logger.addHandler(file_handler)
