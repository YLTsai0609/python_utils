from typing import List

import pendulum


def get_datespan_int(
    start=pendulum.date(2020, 12, 20),
    end=pendulum.date(2021, 1, 29),
    range_unit: str = "days",
    range_num: int = 1,
) -> List[int]:
    datespan = pendulum.period(start, end)
    datespan_int = [
        int(d.format("YYYYMMDD")) for d in datespan.range(range_unit, range_num)
    ]
    return datespan_int


def now(fmt="%m-%d-%H-%M-%S") -> str:
    return pendulum.now().strftime(fmt)
