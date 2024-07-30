import os
import csv
from datetime import datetime
from weather_record import WeatherRecord

class FileParser:
    def __init__(self, directory, year):
        self.directory = directory
        self.year = year

    def parse_files(self):
        weather_records = []

        for filename in os.listdir(self.directory):
            if not filename.startswith(f'Murree_weather_{self.year}'):
                continue

            file_path = os.path.join(self.directory, filename)
            with open(file_path, 'r') as file:
                reader = csv.DictReader(file)
                for row in reader:
                    try:
                        date = datetime.strptime(row['PKT'], '%Y-%m-%d')
                        max_temp = int(row['Max TemperatureC'])
                        min_temp = int(row['Min TemperatureC'])
                        max_humidity = int(row['Max Humidity'])
                        weather_records.append(
                            WeatherRecord(
                                date=date,
                                max_temp=max_temp,
                                min_temp=min_temp,
                                max_humidity=max_humidity
                            )
                        )
                    except (ValueError, KeyError):
                        
                        continue

        return weather_records

