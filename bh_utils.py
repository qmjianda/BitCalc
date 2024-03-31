
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

def styleS_sheet_loder(path: str) -> str:
     with open(path) as fd:
          return fd.read()