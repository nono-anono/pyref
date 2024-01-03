import framework

def retry_init(retry_max_counter,retry_init_flag,retry_init_counter):
    if int(retry_init_counter) < int(retry_max_counter):
        retry_init_counter += 1
        framework.kill_all_processes
        retry_init_flag = True
    else:
        retry_init_flag = False
    
    return retry_init_flag, retry_init_counter
