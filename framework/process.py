from flows import *
from setup import logger

def process(t_item):
    logger.log.info(f"Process started for '{t_item}'...")
    raise ValueError("oopsie")
    some_custom_workflow()
    