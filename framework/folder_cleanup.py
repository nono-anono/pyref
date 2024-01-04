import shutil
import os
from setup import logger

def folder_cleanup(folder_list:list = []):
    logger.log.info(f"Cleaning {len(folder_list)} folder(s)..." if folder_list != [] else "No folders to clean...")
    for folder in folder_list:
        shutil.rmtree(folder)
        os.mkdir(folder)
        logger.log.info(f"Folder '{folder}' was cleaned")

