from sys import exc_info
from e_com_system import ins_logger

def generate_exception(e):
    exc_type, exc_value, exc_traceback = exc_info()
    context= {
        'success':False,
        'details':f"Exception at {str(exc_traceback.tb_frame.f_code.co_filename)} line {str(exc_traceback.tb_lineno)}" if exc_traceback else ''
    }
    ins_logger.logger.error(
        e,
        extra=context
    )