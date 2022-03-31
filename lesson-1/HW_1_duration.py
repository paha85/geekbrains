duration = int(input('please print duration: '))
while duration >= 0:
    days = duration // 86400
    hours = (duration % 86400) // 3600
    minutes = (duration % 3600) // 60
    seconds = (duration % 60) // 1
    if duration >= 86400:
        print(days, 'day(s)', hours, 'hour(s)', minutes, 'minute(s)', seconds, 'second(s)')
    elif 3600 <= duration < 86400:
        print(hours, 'hour(s)', minutes, 'minute(s)', seconds, 'second(s)')
    elif 60 <= duration < 3600:
        print(minutes, 'minute(s)', seconds, 'second(s)')
    else:
        print(seconds, 'second(s)')
    duration = int(input('please print duration or enter "000" to quite: '))
    if duration == 000:
        break
