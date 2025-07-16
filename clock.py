from datetime import datetime

def radian_clock(time = datetime.now()):
    time_in_radians = (time.hour + (time.minute / 60)) / 24 * (2 * 3.14)
    return time_in_radians
