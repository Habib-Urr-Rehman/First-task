# date_utilities.py
def parse_year_month(date_str):
    try:
        year, month = date_str.split('/')
        return int(year), int(month)
    except ValueError:
        raise ValueError("Date must be in the format 'year/month'")
