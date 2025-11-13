# Import necessary packages
from pathlib import Path
from datetime import datetime
import os


# Project imports
from src.utils.colors import color


# Default configurations
_LOG_DIR = Path(os.getenv("LOG_DIR", "logs"))

# RGB strings used by src.utils.colors.color to produce 24-bit ANSI colors
_COLORS = {
    "DEBUG": "0; 255; 255",
    "INFO": "0; 255; 200",
    "SUCCESS": "0; 255; 0",
    "WARNING": "255; 255; 0",
    "ERROR": "255; 0; 0",
    "CRITICAL": "255; 0; 0"
}

# Output format and timestamp format used for each log line
DEFAULT_FORMAT = "{time} | {level} | {name} - {message}"
DATE_FORMAT = "%Y-%m-%d %H:%M:%S"


# Function to ensure that log directory exists
# NOT GOING TO BE USED AT THE MOMENT
def _ensure_log_dir():
    try:
        _LOG_DIR.mkdir(parents=True, exist_ok=True)
    except Exception:
        pass


# Logger class
class __logger():

    def _log(self, level: str, name: str, message: str):
        current_time = datetime.now().strftime(DATE_FORMAT)
        placeholders = [
            ("{time}", current_time),
            ("{level}", color(f"{level:<8}", _COLORS[level])),
            ("{name}", name),
            ("{message}", message)
        ]
        fmt = DEFAULT_FORMAT
        for placeholder in placeholders:
            fmt = fmt.replace(f"{placeholder[0]}", f"{placeholder[1]}")

        print(fmt)

    # Info-level logging. 'name' typically is module or logger name.
    def info(self, name: str, message: str):
        self._log("INFO", name, message)

    # Debug-level logging for verbose diagnostic output.
    def debug(self, name: str, message: str):
        self._log("DEBUG", name, message)

    # Success-level logging for positive confirmations (optional level).
    def success(self, name: str, message: str):
        self._log("SUCCESS", name, message)

    # Warning-level logging for recoverable or noteworthy conditions.
    def warn(self, name: str, message: str):
        self._log("WARNING", name, message)

    # Error-level logging for reported errors.
    def error(self, name: str, message: str):
        self._log("ERROR", name, message)

    # Critical-level logging for severe failures.
    def critical(self, name: str, message: str):
        self._log("CRITICAL", name, message)


# Module-level logger instance to import and use across the project.
log = __logger()
