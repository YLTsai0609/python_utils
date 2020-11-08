'''
===================================================
python常用函數
===================================================
EXPLANATION:
	包含了 IO : 路徑,檔案,圖片檔案, 資料夾,
                  python原生資料結構
                 線程
                 Exception
INPUTS:
	
OPTIONAL INPUT:
	
OPTIONAL INPUT KEYWORD:
	
OUTPUT:
	
EXAMPLE:
	
REVISION HISTORY:
'''


from typing import Generator, List, Tuple
import logging
import threading
import os
import linecache
import sys
import re
import itertools
from collections import deque
import glob
################################## python data structure ############################


def isListEmpty(inList: List[list]) -> bool:
    """
    check a nested list is empty or not.

    Args:
        inList (List[list]): nested list

    Returns:
        bool: true/false
    """
    if isinstance(inList, list):
        return all(map(isListEmpty, inList))
    return False  # Not a list


class SliceableDeque(deque):
    """
    複寫deque的__getitem__，讓你的deque可以坐slicing

    Examples:
        d = SliceableDeque([i for i in range(5)],maxlen=5)
        d[3:5]
        [3,4] (被切割下來的資料會存在list中而非deque中)

    """

    def __getitem__(self, s):
        try:
            start, stop, step = s.start or 0, s.stop or sys.maxsize, s.step or 1
        except AttributeError:  # not a slice but an int
            return super().__getitem__(s)
        else:
            try:
                return list(itertools.islice(self, start, stop, step))
            except ValueError:  # incase of a negative slice object
                length = len(self)
                start, stop = length + start if start < 0 else start, length + \
                    stop if stop < 0 else stop
                return list(itertools.islice(self, start, stop, step))

################################## python data structure ############################

################################## path, file, folder #################################


def absoluteFilePaths(directory: str) -> Generator[str, None, None]:
    """
    generate abosulte path 

    Args:
        directory (str): input

    Yields:
        Generator[str, None, None]: a generator of given directory

    Example:
        list(absoluteFilePaths('.'))
    """
    for dirpath, _, filenames in os.walk(directory):
        for f in filenames:
            yield os.path.abspath(os.path.join(dirpath, f))


def get_file_name_without_extension(filename: str) -> str:
    """
    給定的filename，取得沒有副檔名的檔案名稱
    Args:
        filename (str): 有副檔名的檔案名稱

    Returns:
        str: 沒有副檔名的檔案名稱
    """
    right_dot_position = filename.rfind('.')
    return filename[:right_dot_position]


def touch_dir(abspath: str) -> None:
    '''
    check folder exist or not, if not make one
    path : "absolute" path of folder
    '''
    if not os.path.exists(abspath):
        os.mkdir(abspath)


def convert_date_format(date_str: str) -> str:
    '''
    date_str : 06/11 or 06\\11, 06//11
    return 06_11
    '''
    input_format = re.compile(r'\d+\D\d+')
    if not input_format.match(date_str):
        raise NameError(
            'not valid date format, please make date format 06/11, 06//11, or 06\\11')
    pat_month = re.compile(r'(\d+)\D')
    pat_day = re.compile(r'\D(\d+)')
    return pat_month.findall(date_str)[0] + '_' + pat_day.findall(date_str)[0]


def load_images(images_path: str) -> List[str]:
    """
    如果輸入圖片路徑，直接return
    如果輸入filename.txt，讀取每一行放到list中，然後return
    其他情況，將其視為一個資料夾，把裡面所有jpg, png, jpeg結尾的收集起來然後return
    """
    input_path_extension = images_path.split('.')[-1]
    if input_path_extension in ['jpg', 'jpeg', 'png']:
        return [images_path]
    elif input_path_extension == "txt":
        with open(images_path, "r") as f:
            return f.read().splitlines()
    else:
        return glob.glob(
            os.path.join(images_path, "*.jpg")) + \
            glob.glob(os.path.join(images_path, "*.png")) + \
            glob.glob(os.path.join(images_path, "*.jpeg"))


################################## path, file, folder #################################

################################## Thread #########################################


class StoppableThread(threading.Thread):
    """
    Thread class with a stop() method. The thread itself has to check
    regularly for the stopped() condition.
    https://stackoverflow.com/questions/323972/is-there-any-way-to-kill-a-thread
    """

    def __init__(self, *args, **kwargs):
        super(StoppableThread, self).__init__(*args, **kwargs)
        self._stop_event = threading.Event()

    def stop(self):
        self._stop_event.set()

    def stopped(self):
        return self._stop_event.is_set()

################################## Thread #########################################


################################## Exception #####################################


def PrintException(logger: logging.Logger = None) -> None:
    """
    default try - exception cannot display line number. make us hard to track thr problem
    the solution is using this function
    describe in.
    https://stackoverflow.com/questions/14519177/python-exception-handling-line-number

    Examples:
    try:
        print(1/0)
    except:
        PrintException()
    """
    exc_type, exc_obj, tb = sys.exc_info()
    f = tb.tb_frame
    lineno = tb.tb_lineno
    filename = f.f_code.co_filename
    linecache.checkcache(filename)
    line = linecache.getline(filename, lineno, f.f_globals)
    if logger is None:
        print('EXCEPTION IN ({}, LINE {} "{}"): {}'.format(
            filename, lineno, line.strip(), exc_obj))

################################## Exception #####################################

################################## other #########################################


def isnotebook() -> bool:
    '''
    check current running in notebook or python script
    '''
    try:
        shell = get_ipython().__class__.__name__
        if shell == 'ZMQInteractiveShell':
            return True   # Jupyter notebook or qtconsole
        elif shell == 'TerminalInteractiveShell':
            return False  # Terminal running IPython
        else:
            return False  # Other type (?)
    except NameError:
        return False      # Probably standard Python interpreter
