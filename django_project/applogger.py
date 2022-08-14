import os
import logging
from logging.config import fileConfig
import logging.handlers as handlers
import time

os.makedirs("logs", exist_ok=True)
fileConfig('logging_config.ini')
logger = logging.getLogger()