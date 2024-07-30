from .dimension import SIUnits

_EARTH_RADIUS_KM = 6378.137

class GeoConfig:
    EARTH_RADIUS_KM = _EARTH_RADIUS_KM
    EARTH_RADIUS_M = _EARTH_RADIUS_KM * SIUnits.LENGTH.KM

__all__ = ['GeoConfig']
