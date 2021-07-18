from shared.entities import HistoryRow, metadata
from typing import List

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


class DB:
    def __init__(self):
        self.engine = create_engine('sqlite:///tmp/main.db')
        metadata.create_all(self.engine)
        self.session = sessionmaker(bind=self.engine)

    def save_history_data(self, history_data: List[HistoryRow]):
        # TODO UPDATE METHOD
        session = self.session()
        session.add_all(history_data)
        session.commit()
