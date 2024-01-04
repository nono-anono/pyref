from setup import logger

def close_all_apps(proc_to_close:list[str]=[]):
    logger.log.info(f"No apps to close..." if proc_to_close == [] else f"Closing {len(proc_to_close)} processes...") 