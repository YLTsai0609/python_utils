import glob
import os
from typing import Generator, List


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


def touch_dir(abspath: str) -> None:
    """
    check folder exist or not, if not make one
    path : "absolute" path of folder
    """
    if not os.path.exists(abspath):
        os.mkdir(abspath)


def load_images(images_path: str) -> List[str]:
    """
    如果輸入圖片路徑，直接return
    如果輸入filename.txt，讀取每一行放到list中，然後return
    其他情況，將其視為一個資料夾，把裡面所有jpg, png, jpeg結尾的收集起來然後return
    """
    input_path_extension = images_path.split(".")[-1]
    if input_path_extension in ["jpg", "jpeg", "png"]:
        return [images_path]
    elif input_path_extension == "txt":
        with open(images_path, "r") as f:
            return f.read().splitlines()
    else:
        return (
            glob.glob(os.path.join(images_path, "*.jpg"))
            + glob.glob(os.path.join(images_path, "*.png"))
            + glob.glob(os.path.join(images_path, "*.jpeg"))
        )
