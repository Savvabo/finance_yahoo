from sqlalchemy import (TIMESTAMP, Column, Float, Integer, MetaData, String,
                        Table)
from sqlalchemy.orm import mapper

metadata = MetaData()


class HistoryRow:
    def __init__(self, date, open, high, low, close, adj_close, volume, company_name):
        self.date = date
        self.open = open
        self.high = high
        self.low = low
        self.close = close
        self.adj_close = adj_close
        self.volume = volume
        self.company_name = company_name

    def __repr__(self):
        return "<User('%s','%s', '%s', '%s','%s', '%s', '%s','%s')>" % (
            self.date,
            self.open,
            self.high,
            self.low,
            self.close,
            self.adj_close,
            self.volume,
            self.company_name,
        )


HistoryRecord = Table(
    "history_data",
    metadata,
    Column("id", Integer, primary_key=True, autoincrement=True),
    Column("date", TIMESTAMP, nullable=False),
    Column("open", Float, nullable=False),
    Column("high", Float, nullable=False),
    Column("low", Float, nullable=False),
    Column("close", Float, nullable=False),
    Column("adj_close", Float, nullable=False),
    Column("volume", Float, nullable=False),
    Column("company_name", String(10), nullable=False),
)
mapper(HistoryRow, HistoryRecord)
