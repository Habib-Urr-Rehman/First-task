# weather_record.py
from dataclasses import dataclass

@dataclass
class WeatherRecord:
    date: str
    max_temp: float
    min_temp: float
    mean_humidity: float
