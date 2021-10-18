from datetime import timezone, datetime

TIME_FORMAT = '%-I.%M %p'
CLOSED = 'Closed'


def convert_opening_hours(opening_hours_dict):
    """
    main method to convert unix time to readable time format
    against each day.
    """
    time_list = []
    day_hours_dict = {}
    odd_day = False

    for day, hours_list in opening_hours_dict.items():
        _dict, odd_day = get_day_hours_dict(day, hours_list, odd_day)
        day_hours_dict.update(_dict)
        time_list.extend(get_readable_time_list(hours_list))

    return get_opening_hours_per_day(day_hours_dict, time_list)


def get_day_hours_dict(day, hours_list, odd_day):
    hours_list_len = len(hours_list)
    if not hours_list_len:
        odd_day = False
        return {day: hours_list_len}, odd_day

    elif odd_day and hours_list_len % 2:
        odd_day = False
        return {day: hours_list_len - 1}, odd_day

    elif hours_list_len % 2:
        odd_day = True
        return {day: hours_list_len + 1}, odd_day

    else:
        return {day: hours_list_len}, odd_day


def get_readable_time_list(hours_list):
    """
    convert UNIX time to UTC time and store them all in one list.
    """
    utc_time_list = []
    hours_list_len = len(hours_list)
    if not hours_list_len:
        utc_time_list.append(0)
    else:
        for hours in hours_list:
            time_utc = get_utc_time(hours.get('value'))
            utc_time_list.append(time_utc)
    return utc_time_list


def get_opening_hours_per_day(day_hours_dict, time_list):
    """
    return opening hours per day.
    """
    final_dict = {}

    for day, time_counter_per_day in day_hours_dict.items():
        hour_str = None

        # if time_counter_per_day is 0, restaurant is closed.
        if not time_counter_per_day:
            hour_str = CLOSED
            time_list.pop(0)
        else:
            # pop elements from time_list until hours counter becomes zero.
            while time_counter_per_day:
                open_hr, close_hr = (time_list.pop(0), time_list.pop(0))
                time_counter_per_day -= 2  # we're popping 2 elements so decrease counter with 2.

                hour_str = get_hour_str(hour_str, open_hr, close_hr)

        final_dict.update({day.title(): hour_str})

    return final_dict


def get_utc_time(unix_hour):
    """
    convert unix time to utc time and remove extra zer0s.
    """
    return datetime.fromtimestamp(unix_hour, timezone.utc).strftime(TIME_FORMAT).replace('.00', '')


def get_hour_str(hour_str, open_hr, close_hr):
    """
    represents opening hours as string.
    """
    return f'{open_hr} - {close_hr}' if not hour_str else f'{hour_str}, {open_hr} - {close_hr}'
