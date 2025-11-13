from src.utils.env_check import check_env
from src.utils.logger import log
from dotenv import load_dotenv
from src.utils.error_handler import handle_errors

# Loads .env file
load_dotenv()


@handle_errors(re_raise=False, default=None)
def execute():

    # Check if app is ready to run
    check_env()

    log.info("main.py", "All variables in .env file have been checked")
    log.debug("main.py", "All variables in .env file have been checked")
    log.success("main.py", "All variables in .env file have been checked")
    log.warn("main.py", "All variables in .env file have been checked")
    log.error("main.py", "All variables in .env file have been checked")
    log.critical("main.py", "All variables in .env file have been checked")
