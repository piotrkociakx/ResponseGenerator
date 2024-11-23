from datetime import datetime
from pytz import timezone as pytz_timezone

def get(number):
    total_sum = 0
    while number > 0:
        total_sum += number % 10
        number //= 10
    return total_sum

def generate():
    australia_darwin = pytz_timezone("Australia/Darwin")
    now_darwin = datetime.now(australia_darwin)
    x = int((now_darwin - now_darwin.replace(second=0, microsecond=0)).total_seconds() / 60)
    result = (x + 30) + (x - 15) + (x * 2) + get(x)
    return result
def generate_false():
    australia_darwin = pytz_timezone("Australia/Sydney")
    now_darwin = datetime.now(australia_darwin)
    x = int((now_darwin - now_darwin.replace(second=0, microsecond=0)).total_seconds() / 60)
    result = (x + 30) + (x - 15) + (x * 2) + get(x)
    return result
