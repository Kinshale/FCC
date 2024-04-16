days_of_the_week = ['Monday', 'Tuesday', 'Wednsday', 'Thursday', 'Friday', 'Saturday', 'Sunday']

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

def add_time(start, duration, dow = ''):

    cp1 = start.index(':')
    cp2 = duration.index(':')
    PM = start[-2:] == 'PM'

    days, hours, mins = add(int(start[:cp1]) + PM * 12, int(duration[:cp2]), int(start[cp1 + 1: -3]), int(duration[cp2 + 1:]))
    i_dow = find_day(days_of_the_week, dow.lower().capitalize())

    s1 = f'{hours if hours <= 12 else hours - 12}:{mins} {'AM' if hours <= 12 else 'PM'}'
    s2 = '' if i_dow == -1 else f', {days_of_the_week[i_dow]}'
    s3 =  f'{'' if days == 0 else ' (next day)' if days == 1 else f' ({days} days later)'}'

    return s1 + s2 + s3


#Remember to add the project to GitHub
# Manage 12 PM exception 

print(add_time('11:43 AM', '00:20'))
# Returns: 12:03 PM

print(add_time('10:10 PM', '3:30'))
# Returns: 1:40 AM (next day)

print(add_time('11:43 PM', '24:20', 'tueSday'))
# Returns: 12:03 AM, Thursday (2 days later)

print(add_time('6:30 PM', '205:12'))
# Returns: 7:42 AM (9 days later)
