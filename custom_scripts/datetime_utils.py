import pytz
import datetime
import math


def convert_datetime_to_epoch(datetime_value):
    return int(math.modf((datetime_value).timestamp() * 1000)[1])

def convert_utc_to_local(utc_datetime):
    local_tz = pytz.timezone('Asia/Kolkata')
    timezone_delta = str(local_tz.localize(datetime.datetime.utcnow())).split('+')[1].split(':')
    local_time = utc_datetime + datetime.timedelta(hours=int(timezone_delta[0]), minutes=int(timezone_delta[1]))
    return local_time