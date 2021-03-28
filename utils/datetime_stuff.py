from typing import List

import pendulum


def get_datespan_int(
    start=pendulum.date(2020, 12, 20), end=pendulum.date(2021, 1, 29)
) -> List[int]:
    datespan = pendulum.period(start, end)
    datespan_int = [int(d.format("YYYYMMDD")) for d in datespan.range("days", 1)]
    return datespan_int


def now(fmt="%m-%d-%H-%M-%S") -> str:
    return pendulum.now().strftime(fmt)
