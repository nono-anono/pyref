from setup import logger
from framework import retry_current_transaction,close_all_apps,kill_all_processes
from framework.take_screenshot import take_screenshot
from datetime import datetime

def set_transaction_status(t_number:int,retry_count:int,max_retry_count:int=0,
        system_exception:Exception=None, business_exception:ValueError=None,proc_to_close:list=[],proc_to_kill:list=[]):
    # Success branch
    if system_exception is None and business_exception is None:
        logger.log.info("Transaction process status: Success")
        t_number += 1
        retry_count = 0

    # Business exception branch
    elif business_exception is not None:
        logger.log.info("Transaction process status: Business Exception")
        t_number += 1
        retry_count = 0

    # System exception branch
    else:
        t_number,retry_count = retry_current_transaction(t_number,retry_count,max_retry_count)
        logger.log.info("Transaction process status: System Exception")
        
        try:
            now = datetime.now().strftime('%Y%m%d_%H%M%S')
            file_name = f"{now}_exception.png"
            folder_name = ".logs"
            take_screenshot(folder_name,file_name)
        except Exception as e:
            logger.log.warning(f"Failed to take screenshot: {e}")

        try:
            close_all_apps()
        except Exception as e:
            logger.log.warning(f"Failed to close applications: {e}")
            try:
                kill_all_processes(proc_to_kill)
            except Exception as e:
                logger.log.warning(f"Failed to kill applications: {e}")
    
    return t_number,retry_count