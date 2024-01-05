from setup import logger
from helium import start_chrome,click

def init_all_apps(url:str,):
    logger.log.info("Initializing applications...")
    
    browser = start_chrome(url, headless=False,maximize=True,)
    click('Start')

    return browser