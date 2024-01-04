import framework
from setup import logger

def retry_init(retry_max_counter:int,retry_init_flag:bool,retry_init_counter:int):
    if int(retry_init_counter) < int(retry_max_counter):
        retry_init_counter += 1
        framework.kill_all_processes()
        retry_init_flag = True
        logger.log.warning(f"Try number {retry_init_counter} failed. Retrying..." )
    else:
        retry_init_flag = False
        logger.log.warning(f"Max init retry counter exceeded, process will now end." )
    return retry_init_flag, retry_init_counter
