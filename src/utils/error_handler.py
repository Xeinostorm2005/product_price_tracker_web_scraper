# Standard imports
import functools
import traceback
import os

# Project imports
from src.utils.custom_errors import MissingVariablesInEnv
from src.utils.colors import color
from src.utils.logger import log


# Decorator factory that creates error handlers for functions. Catches and logs
# exceptions, with special handling for custom errors and optional re-raising.
def handle_errors(re_raise: bool = False, default: None = None):

    # Get current environment setting to determine error display behavior
    APP_ENV = os.getenv("APP_ENV")

    def decorator(fn):
        @functools.wraps(fn)
        def wrapper(*args, **kwargs):
            try:
                # Execute the wrapped function with provided arguments
                return fn(*args, **kwargs)
            except MissingVariablesInEnv as e:
                # Log custom error without full traceback for cleaner output
                log.error(fn.__name__, f"{e}")

                # Show detailed error output in development environment only
                if APP_ENV is not None and APP_ENV.upper() == "DEVELOPMENT":
                    print(color(f"Error: {e} \n{e.variables}", fg="255; 0; 0"))
            except Exception as exc:
                # Capture and log full traceback for unexpected errors
                tb = traceback.format_exc()
                log.error(fn.__name__, f"{exc}\n{tb}")
                # Re-raise the exception if configured to do so
                if re_raise:
                    raise
                # Return default value when suppressing exceptions
                return default
        return wrapper
    return decorator
