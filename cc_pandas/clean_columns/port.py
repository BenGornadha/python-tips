from abc import ABC, abstractmethod


class ColumnFormatter(ABC):

    @abstractmethod
    def convert(self, column_name: str) -> str:
        ...
