import os
import sys
from weather_parser import WeatherParser
from date_utils import get_month_name
from data_printer import print_weather_report

def read_weather_data(directory, year, month):
    weather_data = []
    for filename in os.listdir(directory):
        if filename.endswith(".txt"):
            filepath = os.path.join(directory, filename)
            records = WeatherParser.parse_file(filepath)
            weather_data.extend(records)
    return [record for record in weather_data if record.date.year == year and record.date.month == month]

def main():
    if len(sys.argv) != 4 or sys.argv[2] != '-c':
        print("Usage: python main.py /path/to/files-dir -c YYYY/MM")
        return
    
    directory = sys.argv[1]
    year_month = sys.argv[3]
    try:
        year, month = map(int, year_month.split('/'))
    except ValueError:
        print("Error: Year and month should be in YYYY/MM format.")
        return

    weather_data = read_weather_data(directory, year, month)
    
    month_name = get_month_name(year, month)
    print(f"{month_name} {year}")
    
    print_weather_report(weather_data)

if __name__ == "__main__":
    main()
