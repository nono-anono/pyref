from framework import *
from workflows import *
from transitions import Machine
import json
import logging
import os
from datetime import datetime
from pathlib import Path

class Bot:
    # region - Global variables
    config = {}
    setup = {}

    system_exception: Exception = None
    business_exception: ValueError = None

    transaction_data = None
    transaction_item = None
    transaction_number = 1

    retry_item_counter = 0
    retry_init_counter = 0
    retry_init_flag = False
    # endregion

    # region - States 'entry' methods:
    def on_enter_init():
        try:
            Bot.config = {}
            Bot.system_exception = None

            init_all_settings(Bot.config)
            kill_all_processes()
            cleanup()
            Bot.transaction_data = create_transaction_data()
            init_all_apps()
        except Exception as e:
            Bot.system_exception = e
            Bot.retry_init_flag,Bot.retry_init_counter = retry_init(Bot.config['MAX_RETRY_INIT_NUMBER'],Bot.retry_init_flag,Bot.retry_init_counter)

    def on_enter_get():
        try:
            Bot.transaction_item = get_transaction_data(Bot.transaction_data,Bot.transaction_item,Bot.transaction_number)
        except Exception as e:
            print(f"placehodler - exception message in get transaction: {e}")

    def on_enter_process():
        try:
            Bot.business_exception = None
            process(Bot.config,Bot.transaction_item)
        except ValueError as be:
            Bot.business_exception = be
        except Exception as se:
            Bot.system_exception = se
        finally:
            Bot.transaction_number,Bot.retry_item_counter = set_transaction_status(Bot.system_exception,Bot.business_exception,Bot.transaction_number,Bot.retry_item_counter)


    def on_enter_end():
        try:
            close_all_apps()
        except Exception as e:
            print(f"Apps failed to close gracefully. {e} at Source: {e.__traceback__}")
            kill_all_processes()
        
        if Bot.system_exception is not None:
            raise Bot.system_exception

        end_process()
    # endregion

    # region - Transition condition checks
    def init_OK():
        return Bot.system_exception == None

    def init_Retry():
        return Bot.retry_init_flag

    def init_SE():
        return Bot.system_exception != None

    def new_data():
        return Bot.transaction_item != None

    def no_data():
        return Bot.transaction_item == None

    def process_OK():
        return Bot.system_exception == None and Bot.business_exception == None

    def process_BE():
        return Bot.business_exception != None

    def process_SE():
        return Bot.system_exception != None
    # endregion

    # region - Helper methods
    def get_logger():
    # Define the directory and file format
        log_dir = os.path.join(os.getenv('LOCALAPPDATA'), 'pyref', 'logs')
        log_file_name = datetime.now().strftime('%Y-%m-%d_execution.log')
        log_file_path = os.path.join(log_dir, log_file_name)

        # Ensure the directory exists
        os.makedirs(log_dir, exist_ok=True)

        # Define a formatter
        formatter = logging.Formatter('%(asctime)s,%(levelname)s,%(message)s', datefmt='%Y-%m-%d %H:%M:%S')

        # Create handlers
        console_handler = logging.StreamHandler()
        console_handler.setFormatter(formatter)

        file_handler = logging.FileHandler(log_file_path)
        file_handler.setFormatter(formatter)

        # Create a logger with the name 'pyref'
        logger = logging.getLogger('pyref')
        logger.propagate = False
        logger.setLevel(logging.DEBUG)  # Set the logging level
        
        # Add handlers only if no handlers are present
        if not logger.handlers:
            logger.addHandler(console_handler)
            logger.addHandler(file_handler)

        return logger
    log = get_logger()
    # endregion
# region - Main
if __name__ == "__main__":
    
    with open('project.json','r') as file:
        Bot.setup = json.load(file)

    Bot.log.info(f"Project started: {Bot.setup['project_name']}")

    Machine(
        model=Bot,
        states=Bot.setup['states'],
        transitions=Bot.setup['transitions'],
        auto_transitions=False,
        initial='start'
        )
    
    while Bot.state != 'end':
        Bot.trigger('next')
    
    Bot.log.info(f"Project ended: {Bot.setup['project_name']}")
# endregion