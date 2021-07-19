import datetime

from shared.const import date_format
from shared.entities import HistoryRecord


def row_to_dict(row):
    result = {}
    for column in get_history_columns():
        value = getattr(row, column)
        if isinstance(value, datetime.date):
            value = value.strftime(date_format)
        result[column] = value
    return result


def get_history_columns():
    columns = [column.name for column in HistoryRecord.columns]
    return columns
