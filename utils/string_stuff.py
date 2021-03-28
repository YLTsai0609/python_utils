import re


def get_file_name_without_extension(filename: str) -> str:
    """
    給定的filename，取得沒有副檔名的檔案名稱
    Args:
        filename (str): 有副檔名的檔案名稱

    Returns:
        str: 沒有副檔名的檔案名稱
    """
    right_dot_position = filename.rfind(".")
    return filename[:right_dot_position]


def convert_date_format(date_str: str) -> str:
    """
    date_str : 06/11 or 06\\11, 06//11
    return 06_11
    """
    input_format = re.compile(r"\d+\D\d+")
    if not input_format.match(date_str):
        raise NameError(
            "not valid date format, please make date format 06/11, 06//11, or 06\\11"
        )
    pat_month = re.compile(r"(\d+)\D")
    pat_day = re.compile(r"\D(\d+)")
    return pat_month.findall(date_str)[0] + "_" + pat_day.findall(date_str)[0]
