from setup import logger
import subprocess

def kill_all_processes(proc_to_kill:list[str]=[]):

    logger.log.info(f"Killing {len(proc_to_kill)} processes..." if proc_to_kill != [] else "No processes to kill...")
    
    for item in proc_to_kill:
        process = f"{item}.exe"
        subprocess.run(['taskkill','/f','/im',f'{process}'])
        logger.log.info(f"All instances of '{process}' have been terminated.")