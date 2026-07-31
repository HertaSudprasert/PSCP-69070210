"""airport"""

from datetime import datetime
from math import ceil

timein = float(input())
timeout = float(input())

parking_time = timeout - timein

kar_jord_rod = {
    1: 25,
    2: 50,
    3: 80,
    4: 110,
    5: 145,
    6: 180,
    7: 250
}

def jord_rod(time: float):
    """cum nuan kar jord rod jak vela"""
