from setup import logger
from collections import namedtuple

def retry_current_transaction(t_number:int,retry_item_counter:int,max_retry_count:int=0):
    if max_retry_count == 0:
        logger.log.info("Transaction item retries not allowed.")
    else:
        if retry_item_counter >= max_retry_count:
            logger.log.info("Maximum retries per transaction reached")
            retry_item_counter = 0
            t_number += 1
        else:
            logger.log.info("Retrying transaction")
            retry_item_counter += 1

    return t_number,retry_item_counter