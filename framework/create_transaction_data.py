from setup import logger
from flows import *
import os

def create_transaction_data(download_url:str,filename:str,dest_folder:str):
    get_file_by_url(download_url,filename,dest_folder)

    file_path = os.path.abspath(f"{dest_folder}\\{filename}")
    transaction_data = read_excel_file(file_path)

    return transaction_data