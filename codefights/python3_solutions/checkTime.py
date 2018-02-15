#Check if the given string is a correct time representation of the 24-hour clock.

def validTime(ti):
    import time
    fmt = '%H:%M'
    try:
        time.strptime(ti,fmt)
        return True
    except ValueError:
        return False