import sys
from networksecurity.logging import logger  # Assuming this is your logger instance

class NetworkSecurityException(Exception):
    def __init__(self, error_message, error_details: sys):
        self.error_message = str(error_message)

        # Extract traceback info
        _, _, exc_tb = error_details.exc_info()
        if exc_tb:
            self.lineno = exc_tb.tb_lineno
            self.filename = exc_tb.tb_frame.f_code.co_filename
        else:
            self.lineno = None
            self.filename = None

    def __str__(self):
        return f"Error occurred in script name [{self.filename}] line number [{self.lineno}] error message [{self.error_message}]"


