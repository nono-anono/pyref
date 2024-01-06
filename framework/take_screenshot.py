from setup import logger
from datetime import datetime
import mss
import os

def take_screenshot(ss_folder:str,ss_file_name:str):
    
    if ss_folder != "":
        os.makedirs(ss_folder, exist_ok=True)
    
    with mss.mss() as sct:

        for num,monitor in enumerate(sct.monitors[1:],start=1):

            ss_path = f"{ss_folder}\\{num}_{ss_file_name}"
            ss = sct.grab(monitor)
            output = ss_path
            mss.tools.to_png(ss.rgb,ss.size,output=output)
            logger.log.info(f"Screenshot saved at: {ss_path}")