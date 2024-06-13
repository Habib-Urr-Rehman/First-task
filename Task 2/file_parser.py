# file_parser.py
import os
import pandas as pd
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
                df = pd.read_csv(file_path, parse_dates=['PKT'], dayfirst=True, error_bad_lines=False)
                df = df[['PKT', 'Max TemperatureC', 'Min TemperatureC', 'Mean Humidity']]
                
                for _, row in df.iterrows():
                    if pd.notna(row['Max TemperatureC']) and pd.notna(row['Min TemperatureC']) and pd.notna(row['Mean Humidity']):
                        weather_records.append(WeatherRecord(
                            date=row['PKT'],
                            max_temp=row['Max TemperatureC'],
                            min_temp=row['Min TemperatureC'],
                            mean_humidity=row['Mean Humidity']
                        ))
            except Exception as e:
                print(f"Error processing file {file_path}: {e}")

        return weather_records
