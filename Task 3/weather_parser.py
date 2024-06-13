import os
from datetime import datetime
from weather_record import WeatherRecord

class WeatherParser:
    @staticmethod
    def parse_file(filepath):
        records = []
        with open(filepath, 'r') as file:
            for line in file:
                fields = line.strip().split(',')
                date_str = fields[0]
                try:
                    date = datetime.strptime(date_str, '%Y-%m-%d')
                except ValueError:
                    continue
                try:
                    max_temp = int(fields[1])
                    min_temp = int(fields[3])
                    record = WeatherRecord(date, max_temp, min_temp)
                    records.append(record)
                except (ValueError, IndexError):
                    continue
        return records
