from setup import logger

def get_transaction_data(t_data,t_item,t_number:int):

    if t_number <= len(t_data):
        t_item = t_data[t_number - 1]
    else:
        logger.log.info("No more transaction items. Ending the process")
        t_item = None
    
    if t_item is not None:
        logger.log.info(f"Transaction item value:\n{t_item}")

    return t_item