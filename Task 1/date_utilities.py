from datetime import datetime

class DateUtilities:
    @staticmethod
    def format_date(date):
        return date.strftime("%B %d")
