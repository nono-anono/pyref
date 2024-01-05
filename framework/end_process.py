from setup import logger
from framework import close_all_apps
from datetime import datetime
from helium import kill_browser,get_driver
from time import sleep

def end_process():
    
    now = datetime.now().strftime('%Y%m%d_%H%M%S')
    file_name = f"{now}_congrats.png"
    folder_name = "data\\output"
    driver = get_driver()
    driver.save_screenshot(f"{folder_name}\\{file_name}")

    try:    
        sleep(1)
        kill_browser()
    except:
        pass