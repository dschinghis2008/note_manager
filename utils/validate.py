from datetime import datetime


def check_dt_format(date_str, format):
    try:
        datetime.strptime(date_str, format)
        return True
    except ValueError:
        return False


def check_status(status):
    if status in ('new', 'inproc', 'closed'):
        return True
    else:
        return False
