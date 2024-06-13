from datetime import datetime

def get_month_name(year, month):
    return datetime(year, month, 1).strftime('%B')