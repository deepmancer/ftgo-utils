from math import radians, cos, sin, asin, sqrt
from typing import Union, Tuple

from geojson import Point

from ..constants import GeoConfig, SIUnits


def _haversine_flatten(lat1: float, lon1: float, lat2: float, lon2: float, unit: float = SIUnits.LENGTH.KM) -> float:
    lat1, lon1, lat2, lon2 = map(radians, [lat1, lon1, lat2, lon2])
    dlat = lat2 - lat1
    dlon = lon2 - lon1
    a = sin(dlat / 2) ** 2 + cos(lat1) * cos(lat2) * sin(dlon / 2) ** 2
    c = 2 * asin(sqrt(a))
    distance_km = GeoConfig.EARTH_RADIUS_KM * c
    return distance_km * SIUnits.LENGTH.KM / unit

def _haversine_pointwise(p1: Point, p2: Point, unit: float = SIUnits.LENGTH.KM) -> float:
    return _haversine_flatten(p1.coordinates[1], p1.coordinates[0], p2.coordinates[1], p2.coordinates[0], unit=unit)

def _haversine_tuple(coord1: Tuple[float, float], coord2: Tuple[float, float], unit: float = SIUnits.LENGTH.KM) -> float:
    return _haversine_flatten(coord1[0], coord1[1], coord2[0], coord2[1], unit=unit)

def haversine(*args: Union[float, Point, Tuple[float, float]], unit: float = SIUnits.LENGTH.KM) -> float:
    if len(args) == 2:
        if isinstance(args[0], Point) and isinstance(args[1], Point):
            return _haversine_pointwise(*args, unit=unit)
        elif isinstance(args[0], tuple) and isinstance(args[1], tuple):
            return _haversine_tuple(*args, unit=unit)
    elif len(args) == 4 and all(isinstance(arg, (int, float)) for arg in args):
        return _haversine_flatten(*args, unit=unit)
    else:
        raise ValueError("Invalid arguments for haversine function")


__all__ = ['haversine']
