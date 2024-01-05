from setup import *
from framework import *
from flows import *

class bot(state_machine,transitions):
    # region - Global variables
    
    config = {}
    project_name:str = 'pyref'

    system_exception = None
    business_exception = None

    transaction_data = object
    transaction_item = object
    transaction_number:int  = 1

    retry_item_counter:int  = 0
    retry_init_counter:int  = 0
    retry_init_flag:bool = False

    processes_to_kill:list[str] = []
    folders_to_clean:list = ['data\\output','data\\temp']
    # endregion

    # region - States 'entry' methods:
    def on_enter_init(**kwargs):
        try:
            bot.system_exception = None

            if bot.config == {}:
                init_all_settings(bot.config)
                kill_all_processes()
                folder_cleanup(bot.folders_to_clean)

            bot.transaction_data = create_transaction_data(bot.config['URL_EXCEL_FILE'],'challenge.xlsx','data\\temp')
            bot.browser =  init_all_apps(bot.config['URL_SITE'])
        except Exception as e:
            bot.system_exception = e
            bot.retry_init_flag,bot.retry_init_counter = retry_init(bot.config['MAX_RETRY_INIT'],bot.retry_init_flag,bot.retry_init_counter)

    def on_enter_get(**kwargs):
        try:
            bot.transaction_item = get_transaction_data(bot.transaction_data,bot.transaction_item,bot.transaction_number)
        except Exception as e:
            logger.log.error(f"Error processing transaction #{bot.transaction_number}\nException: {e}")
            raise e


    def on_enter_process(**kwargs):
        try:
            bot.business_exception = None
            process(bot.transaction_item,bot.transaction_number)
        except ValueError as be:
            bot.business_exception = be
            logger.log.error(be)
        except Exception as se:
            bot.system_exception = se
            logger.log.error(se)
        finally:
            bot.transaction_number,bot.retry_item_counter = set_transaction_status(
                    bot.transaction_number,
                    bot.retry_item_counter,
                    int(bot.config['MAX_RETRY_TRANSACTION']),
                    bot.system_exception,
                    bot.business_exception
                    )

    def on_enter_end(**kwargs):
        try:
            close_all_apps()
        except Exception as e:
            logger.log.warning(f"Apps failed to close gracefully: {e}")
            kill_all_processes(bot.processes_to_kill)
        
        if bot.system_exception is None:
            end_process()
            logger.log.info(f"Project ended: {bot.project_name}")
        else:
            logger.log.error(f"System exception at initialization: {bot.system_exception}")
            raise bot.system_exception
    # endregion

# Main entry point
if __name__ == "__main__":
    logger.log.info(f"Project started: {bot.project_name}")
    state_machine.run(bot)