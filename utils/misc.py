import linecache
import logging
import sys
import threading


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
        print(
            'EXCEPTION IN ({}, LINE {} "{}"): {}'.format(
                filename, lineno, line.strip(), exc_obj
            )
        )


################################## Exception #####################################

################################## other #########################################


def isnotebook() -> bool:
    """
    check current running in notebook or python script
    """
    try:
        shell = get_ipython().__class__.__name__
        if shell == "ZMQInteractiveShell":
            return True  # Jupyter notebook or qtconsole
        elif shell == "TerminalInteractiveShell":
            return False  # Terminal running IPython
        else:
            return False  # Other type (?)
    except NameError:
        return False  # Probably standard Python interpreter
