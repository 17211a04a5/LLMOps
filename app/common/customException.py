import sys

class CustomException(Exception):
    def __init__(self, message, error_detail: sys):
        super().__init__(message)
        self.error_detail = self.get_detailed_error_message(message, error_detail)

    @staticmethod
    def get_detailed_error_message(message, error_detail):
        _, _, exc_tb = sys.exc_info()
        file_name = exc_tb.tb_frame.f_code.co_filename if exc_tb else "Unknown"
        line_number = exc_tb.tb_lineno if exc_tb else "Unknown"
        error_message = f"Error occurred in file: {file_name} at line: {line_number} with message: {message} error detail: {str(error_detail)}"
        return error_message
    
    def __str__(self):
        return f"{self.error_detail}: {super().__str__()}"