from main import bot
import subprocess

def kill_all_processes(proc_list:list=[]):
    bot.log.info(f"Killing {len(proc_list)} processes..." if proc_list != [] else "No processes to kill...")
    
    for item in proc_list:
        process = f"{item}.exe"
        subprocess.run(['taskkill','/f','/im',f'{process}'])
        bot.log.info(f"All instances of '{process}' have been terminated.")