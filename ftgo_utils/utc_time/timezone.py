import pytz
from datetime import datetime

def now():
    return datetime.now(pytz.UTC)

def now_timestamp():
    return int(datetime.now(pytz.UTC).timestamp())

timezone = pytz.UTC
