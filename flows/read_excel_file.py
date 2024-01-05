from setup import logger
from pylightxl import readxl

def read_excel_file(file_path:str):
    try:
        raw_data = []
        file = readxl(file_path)

        for row in file.ws('Sheet1').rows:
            raw_data.append(row)

        headers = [header.strip() for header in raw_data[0]]
        
        transaction_data = [dict(zip(headers,row)) for row in raw_data[1:]]
        logger.log.info(f"Successfully read excel file. Row count: {len(transaction_data)}")
    except Exception as e:
        logger.log.error(f"Failed to read excel file: {e}")
        raise e

    return transaction_data