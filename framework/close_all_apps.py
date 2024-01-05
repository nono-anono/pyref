from setup import logger
from helium import kill_browser
def close_all_apps():
    # helium automatically closes browser on process end, no need to implement logic for closing browser
    kill_browser()