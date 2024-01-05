from setup import logger
from datetime import datetime
from PIL import ImageGrab
import os

def take_screenshot(ss_folder:str,ss_file_name:str):
    
    if ss_folder != "":
        os.makedirs(ss_folder, exist_ok=True)

    ss_path = os.path.join(ss_folder,ss_file_name)
    
    ImageGrab.grab().save(ss_path)

    logger.log.info(f"Screenshot saved at: {ss_path}")