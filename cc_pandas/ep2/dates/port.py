from abc import ABC, abstractmethod
from typing import Optional


class DateHandler(ABC):
    @abstractmethod
    def normalize_dates(self, date_format: str = "%Y-%m-%d") -> None:
        pass

    @abstractmethod
    def validate_dates(self) -> bool:
        pass

    @abstractmethod
    def filter_outliers(self, start_date: Optional[str] = None, end_date: Optional[str] = None) -> None:
        pass