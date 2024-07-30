from math import fabs
from typing import Optional

from .dimension import SIUnits

class BaseLengthConfig:
    _resolution_mapping = {}

    @classmethod
    def get_closest_resolution(cls, length: float) -> Optional[int]:
        differences = {resolution: fabs(length - mapped_length) for resolution, mapped_length in cls._resolution_mapping.items()}
        return min(differences, key=differences.get, default=None)

class RadiusLengthConfig(BaseLengthConfig):
    # In KM
    _resolution_mapping = {
        0: 1287.835655657572,
        1: 483.40406249331404,
        2: 182.5316443376397,
        3: 68.98023034462467,
        4: 26.071814134916993,
        5: 9.854093930089253,
        6: 3.7245328257529372,
        7: 1.406475771474197,
        8: 0.5314140078198508,
        9: 0.20078613724380597,
        10: 0.07586377668461957,
        11: 0.028663842408606925,
        12: 0.010830161507766968,
        13: 0.004092312791439107,
        14: 0.0015471659296802671,
        15: 0.0005858760630436926
    }

    @classmethod
    def get_length(cls, resolution: int) -> float:
        return cls._resolution_mapping.get(resolution, 0) * SIUnits.LENGTH.KM

class EdgeLengthConfig(BaseLengthConfig):
    # In KM
    _resolution_mapping = {
        0: 1281.256011,
        1: 483.0568391,
        2: 182.5129565,
        3: 68.97922179,
        4: 26.07175968,
        5: 9.85409099,
        6: 3.724532667,
        7: 1.406475763,
        8: 0.53141401,
        9: 0.200786148,
        10: 0.075863783,
        11: 0.028663897,
        12: 0.010830188,
        13: 0.00409201,
        14: 0.0015461,
        15: 0.000584169
    }

    @classmethod
    def get_length(cls, resolution: int) -> float:
        return cls._resolution_mapping.get(resolution, 0) * SIUnits.LENGTH.KM

class HexagonAreaConfig(BaseLengthConfig):
    # In KM^2
    _resolution_mapping = {
        0: 4_357_449.416078392,
        1: 609_788.441794134,
        2: 86_801.780398997,
        3: 12_393.434655088,
        4: 1_770.347654491,
        5: 252.903858182,
        6: 36.129062164,
        7: 5.16129336,
        8: 0.737327598,
        9: 0.105332513,
        10: 0.015047502,
        11: 0.002149643,
        12: 0.000307092,
        13: 0.00004387,
        14: 0.000006267,
        15: 0.000000895
    }

    @classmethod
    def get_area(cls, resolution: int) -> float:
        return cls._resolution_mapping.get(resolution, 0) * SIUnits.LENGTH.KM ** 2

__all__ = ['RadiusLengthConfig', 'EdgeLengthConfig', 'HexagonAreaConfig']
