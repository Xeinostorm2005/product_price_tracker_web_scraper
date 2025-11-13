# Imports necessary packages
from typing import Literal


# Creates a custom error exception for .env file
class MissingVariablesInEnv(Exception):

    # Default variables
    MESSAGE_NOTFOUND = "Found missing variables in the .env file!"
    MESSAGE_WRONG_TYPE = "Wrong value types in the .env file!"
    ERROR_CODE = 500

    # Initialize Error Exception
    def __init__(
        self,
        error_type: Literal["notfound", "wrong_type"],
        variables: list,
        message: str | None = None,
        code: int | None = None,
    ):
        # Respond with a specific message
        if error_type == "notfound":
            self.message = message or self.MESSAGE_NOTFOUND
        else:
            self.message = message or self.MESSAGE_WRONG_TYPE

        # Returns default or specific error code
        self.code = code or self.ERROR_CODE

        # Shows which variables needs to be updated
        self.variables = variables

        super().__init__(self.message)
