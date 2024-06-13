


import sys
from datetime import datetime
from weather_parser import WeatherParser
from data_printing import generate_bar_chart

def main():
    if len(sys.argv) != 4 or sys.argv[2] != '-c':
        print("Usage: weatherman.py /path/to/files-dir -c YYYY/MM")
        return
    
    directory = sys.argv[1]
    period = sys.argv[3]
    
    try:
        year, month = map(int, period.split('/'))
    except ValueError:
        print("Error: Year and month should be in YYYY/MM format.")
        return
    
    parser = WeatherParser(directory)
    weather_data = parser.read_weather_data(year, month)
    month_name = datetime(year, month, 1).strftime('%B')
    
    print(f"{month_name} {year}")
    generate_bar_chart(weather_data)
    print()

if __name__ == "__main__":
    main()
