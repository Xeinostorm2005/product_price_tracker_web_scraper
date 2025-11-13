# Imports necessary packages
import os

# Import from /src
from src.utils.custom_errors import MissingVariablesInEnv


# Checks if variables in .env are not missing
# and checks if they have the correct value (e.g str, int)
def check_env():

    # Stores found variables that should be updated
    missing_variables = []
    wrong_type_variables = []

    # Stores all necessary variables
    variables: list[tuple] = [
        ("DATABASE_URI", str), ("DATABASE_NAME", str),
        ("REDIS_HOST", str), ("REDIS_PORT", int),
        ("SCRAPING_QUEUE_NAME", str)
    ]

    # Checks if each variables is available and correct value type
    for var_name, var_type in variables:

        # Fetches the value from .env file
        env_variable = os.getenv(f"{var_name}")

        # Checks if value is not None or Empty
        if env_variable is None or env_variable == "":
            missing_variables.append(var_name)

        # Type validation for non-string types
        if env_variable is not None and var_type == int:
            try:
                int(env_variable)
            except ValueError:
                wrong_type_variables.append(var_name)

    # Checks if there are any missing variables
    if len(missing_variables):
        raise MissingVariablesInEnv(
            error_type="notfound",
            variables=missing_variables
        )

    # Checks if there are any variables with wrong type values
    if len(wrong_type_variables):
        raise MissingVariablesInEnv(
            error_type="wrong_type",
            variables=wrong_type_variables
        )
