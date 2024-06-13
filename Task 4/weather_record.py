from datetime import datetime

class WeatherRecord:
    def __init__(self, date, max_temp, min_temp):
        self.date = date
        self.max_temp = max_temp
        self.min_temp = min_temp

    @staticmethod
    def from_string(record_string):
        fields = record_string.strip().split(',')
        date_str = fields[0]
        try:
            date = datetime.strptime(date_str, '%Y-%m-%d')
            max_temp = int(fields[1])
            min_temp = int(fields[3])
            return WeatherRecord(date, max_temp, min_temp)
        except (ValueError, IndexError):
            return None
