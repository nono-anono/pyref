from _setup import *
from framework import *
from workflows import *

class bot(state_machine,transitions):
    # region - Global variables
    log = init_logger()

    project_name:str = 'pyref'

    system_exception = None
    business_exception = None

    transaction_data = None
    transaction_item = None
    transaction_number:int  = 1

    retry_item_counter:int  = 0
    retry_init_counter:int  = 0
    retry_init_flag:bool = False
    # endregion

    # region - States 'entry' methods:
    def on_enter_init(**kwargs):
        try:
            bot.log.info(f"Project started: {bot.project_name}")
            bot.config = {}
            bot.system_exception = None
            init_all_settings(bot.config)
            kill_all_processes()
            folder_cleanup(['data\\output','data\\temp'])
            bot.transaction_data = create_transaction_data()
            init_all_apps()
        except Exception as e:
            bot.system_exception = e
            bot.retry_init_flag,bot.retry_init_counter = retry_init(bot.config['MAX_RETRY_INIT_NUMBER'],bot.retry_init_flag,bot.retry_init_counter)

    def on_enter_get(**kwargs):
        try:
            bot.transaction_item = get_transaction_data(bot.transaction_data,bot.transaction_item,bot.transaction_number)
        except Exception as e:
            print(f"placehodler - exception message in get transaction: {e}")

    def on_enter_process(**kwargs):
        try:
            bot.business_exception = None
            process(bot.config,bot.transaction_item)
        except ValueError as be:
            bot.business_exception = be
        except Exception as se:
            bot.system_exception = se
        finally:
            bot.transaction_number,bot.retry_item_counter = set_transaction_status(bot.system_exception,bot.business_exception,bot.transaction_number,bot.retry_item_counter)


    def on_enter_end(**kwargs):
        try:
            close_all_apps()
        except Exception as e:
            print(f"Apps failed to close gracefully. {e} at Source: {e.__traceback__}")
            kill_all_processes()
        
        if bot.system_exception is None:
            end_process()
            bot.log.info(f"Project ended: {bot.project_name}")
        else:
            raise bot.system_exception
    # endregion

# Main entry point
if __name__ == "__main__":
    state_machine.run(bot)