# weather_parser.py

import os
from weather_record import WeatherRecord

class WeatherParser:
    def __init__(self, directory):
        self.directory = directory

    def read_weather_data(self, year, month):
        weather_data = {}
        for filename in os.listdir(self.directory):
            if not filename.endswith(".txt"):
                continue
            filepath = os.path.join(self.directory, filename)
            with open(filepath, 'r') as file:
                for line in file:
                    record = WeatherRecord.from_string(line)
                    if record and record.date.year == year and record.date.month == month:
                        day = record.date.day
                        if day not in weather_data:
                            weather_data[day] = []
                        weather_data[day].append((record.max_temp, record.min_temp))
        return weather_data
