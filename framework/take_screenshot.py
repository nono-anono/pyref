from setup import logger
from datetime import datetime
from PIL import ImageGrab
import os

def take_screenshot(ss_folder:str):

    now = datetime.now().strftime('%Y%m%d_%H%M%S')

    ss_file_name = f"{now}_exception.png"
    ss_path = os.path.join(ss_folder,ss_file_name)
    
    ImageGrab.grab().save(ss_path)

    logger.log.info(f"Screenshot saved at: {ss_path}")