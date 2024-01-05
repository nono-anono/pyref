from setup import logger
from framework.take_screenshot import take_screenshot
from framework import close_all_apps
from datetime import datetime
def end_process():
    
    now = datetime.now().strftime('%Y%m%d_%H%M%S')
    file_name = f"{now}_congrats.png"
    folder_name = "data\\output"
    take_screenshot(folder_name,file_name)
    
    close_all_apps()