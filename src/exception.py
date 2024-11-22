import sys
from src.logger import logging

def get_error_details(error, error_detail:sys):
    '''
    Constructs a detailed error message.
    '''
    
    _,_, exc_traceback = error_detail.exc_info() # exc_type, exc_value are unused
    file_name = exc_traceback.tb_frame.f_code.co_filename
    line_number = exc_traceback.tb_lineno

    error_message = f"Error occured in script: {file_name} at line {line_number}, message: {str(error)}"

    return error_message


class CustomException(Exception):
    '''
    Custom Exception class to provide detailed error messages.
    '''
    def __init__(self, error_message, error_detail:sys):
        super().__init__(error_message)
        self.error_message = get_error_details(error_message, error_detail)

    def __str__(self):
        return self.error_message