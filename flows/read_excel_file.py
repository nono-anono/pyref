from setup import logger
from pandas import read_excel

def read_excel_file(full_file_path:str):
    try:
        transaction_data = read_excel(full_file_path)
        logger.log.info(f"Successfully read excel file. Row count: {len(transaction_data)}")
    except Exception as e:
        logger.log.error(f"Failed to read excel file: {e}")
        raise e
    
    return transaction_data