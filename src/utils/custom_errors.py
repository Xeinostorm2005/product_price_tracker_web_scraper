# Imports necessary packages
from typing import Literal


# Creates a custom error exception for .env file
class MissingVariablesInEnv(Exception):

    # Default variables
    default_message_notfound = "Found missing variables in the .env file!"
    default_message_wrong_type = "Wrong value types in the .env file!"
    default_error_code = 500

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
            self.message = message or self.default_message_notfound
        else:
            self.message = message or self.default_message_wrong_type

        # Returns default or specific error code
        self.code = code or self.default_error_code

        # Shows which variables needs to be updated
        self.variables = variables

        super().__init__(self.message)
