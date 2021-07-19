import argparse
import datetime
from typing import List

import requests
from shared.const import HEADERS, PARAMS, URL_TEMPLATE
from shared.db import DB
from shared.entities import HistoryRow

parser = argparse.ArgumentParser(description="Process some integers.")
parser.add_argument("company_name", type=str)

db_instant = DB()


def get_historical_data(company_name: str) -> dict:
    link = URL_TEMPLATE.format(company_name)
    response = requests.get(link, headers=HEADERS, params=PARAMS)
    if response.status_code != 200:
        raise Exception("Company {} does not exist".format(company_name))
    return response.json()


def transform_historical_data(company_data: dict) -> List[HistoryRow]:
    drop_down_data = company_data["chart"]["result"][0]
    indicators = drop_down_data["indicators"]
    quote_data = indicators["quote"][0]

    date_col = map(datetime.datetime.fromtimestamp, drop_down_data["timestamp"])

    open_col = map(lambda num: round(num, 2), quote_data["open"])
    high_col = map(lambda num: round(num, 2), quote_data["high"])
    low_col = map(lambda num: round(num, 2), quote_data["low"])
    close_col = map(lambda num: round(num, 2), quote_data["close"])
    adj_close_col = map(
        lambda num: round(num, 2), indicators["adjclose"][0]["adjclose"]
    )
    volume_col = map(lambda num: round(num, 2), quote_data["volume"])

    history_table = zip(
        date_col, open_col, high_col, low_col, close_col, adj_close_col, volume_col
    )
    # get company name from json
    company_name = company_data["chart"]["result"][0]["meta"]["symbol"]
    history_table_rows = list(
        map(
            lambda tuple_row: HistoryRow(*tuple_row, company_name=company_name),
            history_table,
        )
    )
    return history_table_rows


def save_transformed_data_to_db(transformed_data: List[HistoryRow]):
    db_instant.save_history_data(transformed_data)


def run(company_name):
    historical_data = get_historical_data(company_name)
    transformed_data = transform_historical_data(historical_data)
    save_transformed_data_to_db(transformed_data)


if __name__ == "__main__":
    args = parser.parse_args()
    run(args.company_name)
