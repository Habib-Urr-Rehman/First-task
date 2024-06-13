import os
import pandas as pd
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
            df = pd.read_csv(file_path, parse_dates=['PKT'])
            df = df[['PKT', 'Max TemperatureC', 'Min TemperatureC', 'Max Humidity']]

            for _, row in df.iterrows():
                if pd.notna(row['Max TemperatureC']) and pd.notna(row['Min TemperatureC']) and pd.notna(row['Max Humidity']):
                    weather_records.append(
                        WeatherRecord(
                            date=row['PKT'],
                            max_temp=row['Max TemperatureC'],
                            min_temp=row['Min TemperatureC'],
                            max_humidity=row['Max Humidity']
                        )
                    )

        return weather_records
