import logging

def split_string_by_length(string, length) -> str:
    return [string[i:i+length] for i in range(0, len(string), length)]

def repeat_insert_str(src:str, mark:str, step:int, padding="") -> str:
        src_len = len(src)
        if(src_len%step != 0):
            res_str = (step - src_len%step) * padding + src
        else:
             res_str = src
        res_str_list = split_string_by_length(res_str, step)
        return mark.join(res_str_list)

def style_sheet_loder(path: str) -> str:
     with open(path) as fd:
          return fd.read()


logger = logging.getLogger(__name__)
__logger_handler = logging.StreamHandler()
__formatter = logging.Formatter('%(levelname)s: %(message)s')
__logger_handler.setFormatter(__formatter)
logger.addHandler(__logger_handler)
logger.setLevel(logging.DEBUG)