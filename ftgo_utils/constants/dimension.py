class Length:
    M = 1.0
    KM = 1000.0
    MI = 1609.344

class Time:
    SEC = 1.0
    MIN = 60.0
    HOUR = 3600.0
    DAY = 86400.0

class Speed:
    MPS = 1.0
    KPH = 3.6
    MPH = 2.236936
    
class SIUnits:
    LENGTH = Length
    TIME = Time
    SPEED = Speed

__all__ = ['SIUnits']
