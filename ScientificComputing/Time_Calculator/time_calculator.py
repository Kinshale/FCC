days_of_the_week = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

def find_day(a, e):
    try:
        return a.index(e)
    except ValueError:
        return -1

def add(h1, h2, m1, m2):
    h, m = h1 + h2, m1 + m2

    return (
        (h + m // 60) // 24, 
        (h + m // 60) % 24,
        m % 60
    )

def add_time(start, duration, dow = ""):

    cp1 = start.index(":")
    cp2 = duration.index(":")
    PM = start[-2:] == "PM"

    days, hours, mins = add(int(start[:cp1]) + PM * 12, int(duration[:cp2]), int(start[cp1 + 1: -3]), int(duration[cp2 + 1:]))
    i_dow = find_day(days_of_the_week, dow.lower().capitalize())

    if (hours == 0): # handle the fact that 00:03 should be displayed as 12:03 AM
        hours = 24

    s1 = ("0" if hours < 10 else "") + f"{hours if hours <= 12 else hours - 12}" + ":" + ("0" if mins < 10 else "") + f"{mins} " + ("AM" if hours < 12 or hours == 24 else "PM")
    s2 = "" if i_dow == -1 else f", {days_of_the_week[(i_dow + days) % 7]}"
    s3 = "" if days == 0 else " (next day)" if days == 1 else f" ({days} days later)"

    return s1 + s2 + s3

print(add_time('2:59 AM', '24:00', 'saturDay'))
print(add_time('11:55 AM', '3:12'))
print(add_time('8:16 PM', '466:02'))

