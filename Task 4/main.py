


import sys
from weather_parser import WeatherParser
from data_printing import generate_bar_chart
from datetime import datetime

def main():
    if len(sys.argv) < 4 or any(arg not in ['-c', '-a', '-e'] for arg in sys.argv[2::2]):
        print("Usage: weatherman.py /path/to/files-dir -c YYYY/MM -a YYYY/MM -e YYYY")
        return
    
    directory = sys.argv[1]
    parser = WeatherParser(directory)
    reports = {}
    for i in range(2, len(sys.argv), 2):
        arg = sys.argv[i]
        period = sys.argv[i+1]
        if arg == '-c' or arg == '-a':
            try:
                year, month = map(int, period.split('/'))
                weather_data = parser.read_weather_data(year, month)
                month_name = datetime(year, month, 1).strftime('%B')
                reports[f"{month_name} {year}"] = weather_data
            except ValueError:
                print("Error: Year and month should be in YYYY/MM format.")
                return
        elif arg == '-e':
            try:
                year = int(period)
                weather_data = parser.read_weather_data(year, 0)
                reports[str(year)] = weather_data
            except ValueError:
                print("Error: Year should be in YYYY format.")
                return
    
    for period, data in reports.items():
        print(period)
        generate_bar_chart(data)
        print()

if __name__ == "__main__":
    main()
