from typing import List

import pendulum

date = pendulum.date


def get_datespan_int(
    start: date = pendulum.date(2020, 12, 20),
    end: date = pendulum.date(2021, 1, 29),
    range_unit: str = "days",
    range_num: int = 1,
) -> List[int]:
    """
    get dataspan int list from pendulum object

    Args:
    start (date):  Defaults to pendulum.date(2020, 12, 20).
    end (date):  Defaults to pendulum.date(2021, 1, 29).
    range_unit (str):  Defaults to "days".
    range_num (int):  Defaults to 1.

    Returns:
        List[int]:
    """
    datespan = pendulum.period(start, end)
    datespan_int = [
        int(d.format("YYYYMMDD")) for d in datespan.range(range_unit, range_num)
    ]
    return datespan_int


def now(fmt="%m-%d-%H-%M-%S") -> str:
    return pendulum.now().strftime(fmt)
