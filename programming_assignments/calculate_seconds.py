
time_units = ['second', 'minute', 'hour', 'day', 'week', 'month','year']


def calc_num_of_sec (time_period, time_unit):
    if time_unit == 'minute':
        return calc_sec(time_period)

    elif time_unit == 'hour':
        return calc_sec(calc_min(time_period))

    elif time_unit == 'day':
        return calc_sec(calc_min(calc_hrs(time_period)))

    elif time_unit == 'week':
        return calc_sec(calc_min(calc_hrs(calc_day(time_period))))

    elif time_unit == 'month':
        return calc_sec(calc_min(calc_hrs(calc_day(calc_week(time_period)))))

    elif time_unit == 'year':
        return calc_sec(calc_min(calc_hrs(calc_day(calc_week(calc_month(time_period))))))




def calc_sec(m):
    return m*60

def calc_min(h):
    return h*60

def calc_hrs(d):
    return d*24

def calc_day(w):
    return w*7

def calc_week(m):
    return m*30

def calc_year(y):
    return y*12


time_period = int (input ("Enter time period: "))
time_unit = input ("Enter unit: ")

print (calc_num_of_sec(time_period,time_unit))