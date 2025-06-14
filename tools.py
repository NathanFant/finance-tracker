from datetime import date, datetime
from typing import Union


def parse_due_date(due_date: Union[str, int, date, datetime]) -> int:
    """
    Parses the due date from a string, integer, date, or datetime object.
    Returns the day of the month (1-31).
    Accepts:
      - str: 'MM-DD-YYYY' or 'MM-DD-YY'
      - int: day of the month (1-31)
      - date/datetime: extracts `.day`
    """

    if isinstance(due_date, str):  # assuming format 'MM-DD-YYYY' or 'MM-DD-YY'
        for format in ("%m-%d-%Y", "%m-%d-%y"):
            try:
                parsed_date = datetime.strptime(due_date, format)
                return parsed_date.day
            except ValueError:
                continue
        raise ValueError(
            f"String due date '{due_date}' must be in 'MM-DD-YYYY' or 'MM-DD-YY' format."
        )

    elif isinstance(due_date, int):  # assuming integer is the day of the month
        if 1 <= due_date <= 31:
            return due_date
        raise ValueError(f"Integer due date '{due_date}' must be between 1 and 31.")

    elif isinstance(due_date, (date, datetime)):  # assuming date or datetime object
        return due_date.day

    else:  # if the input is not a valid type
        raise ValueError(
            f"Due date of type '{type(due_date)} is not supported. Must be str, int, date, or datetime."
        )
