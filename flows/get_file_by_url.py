import requests
import os
from setup import logger

def get_file_by_url(url:str,filename:str,dest_folder:str):
    try:
        full_path = os.path.join(dest_folder,filename)
        response = requests.get(url)
        response.raise_for_status()

        os.makedirs(dest_folder,exist_ok=True)

        with open(full_path, 'wb') as file:
            file.write(response.content)

        logger.log.info(f"File downloaded successfully: {filename}")

    except requests.exceptions.HTTPError as e:
        logger.log.error(f"Error getting file by url: {e}")
        raise e
        