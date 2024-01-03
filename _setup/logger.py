import logging
import os
from datetime import datetime

def init_logger():
# Define the directory and file format
    log_dir = '.logs'
    # log_dir = os.path.join(os.getenv('LOCALAPPDATA'), 'pyref', 'logs')    << in case you want to save in App/Local folder
    log_file_name = datetime.now().strftime('%Y-%m-%d_Execution.log')
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

    # Create a named logger, to avoid clashing with pytransition's default logger
    logger = logging.getLogger('pyref')
    logger.propagate = False
    logger.setLevel(logging.INFO)  # Set the logging level
    
    # Add handlers only if no handlers are present
    if not logger.handlers:
        logger.addHandler(console_handler)
        logger.addHandler(file_handler)

    return logger
