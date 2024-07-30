


import os
import csv
from datetime import datetime
from weather_record import WeatherRecord

class FileParser:
    def __init__(self, directory):
        self.directory = directory

    def parse_files(self, year, month):
        weather_records = []

        for filename in os.listdir(self.directory):
            if not filename.startswith(f'Murree_weather_{year}_{month}'):
                continue

            file_path = os.path.join(self.directory, filename)
            try:
                with open(file_path, 'r') as file:
                    reader = csv.DictReader(file)
                    for row in reader:
                        try:
                            date = datetime.strptime(row['PKT'], '%Y-%m-%d')
                            max_temp = int(row['Max TemperatureC'])
                            min_temp = int(row['Min TemperatureC'])
                            mean_humidity = int(row['Mean Humidity'])
                            weather_records.append(
                                WeatherRecord(
                                    date=date,
                                    max_temp=max_temp,
                                    min_temp=min_temp,
                                    mean_humidity=mean_humidity
                                )
                            )
                        except (ValueError, KeyError):
                           
                            continue
            except Exception as e:
                print(f"Error processing file {file_path}: {e}")

        return weather_records
