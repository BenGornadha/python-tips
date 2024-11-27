
from abc import ABC, abstractmethod
import pandas as pd
from scipy.stats import kstest, shapiro, anderson



class GaussianChecker(ABC):

    def is_gaussian(self, a_series: pd.Series, min_p_value=0.05) -> bool:
        self._clean_temporary_extreme_values(a_series=a_series)
        return self._check_gaussian(a_series=self._series,
                                    min_p_value=min_p_value)

    @abstractmethod
    def _check_gaussian(self, a_series: pd.Series, min_p_value: float) -> bool:
        raise NotImplementedError

    def _clean_temporary_extreme_values(self, a_series: pd.Series) -> None:
        self._series = a_series[(a_series - a_series.mean()).abs() <= 3.0 * a_series.std()]


class GaussianCheckerKSTest(GaussianChecker):

    def _check_gaussian(self, a_series: pd.Series, min_p_value: float) -> bool:
        stat, p_value = kstest(a_series, 'norm', args=(a_series.mean(), a_series.std()))
        return p_value > min_p_value


class GaussianCheckerShapiro(GaussianChecker):

    def _check_gaussian(self, a_series: pd.Series, min_p_value: float) -> bool:
        stat, p_value = shapiro(x=a_series)
        return p_value > min_p_value


class GaussianCheckerAnderson(GaussianChecker):

    def _check_gaussian(self, a_series: pd.Series, min_p_value: float = 0.05):
        result = anderson(a_series, dist='norm')
        critical_value = result.critical_values[2]
        return result.statistic < critical_value
