import sys
from file_parser import FileParser
from date_utilities import DateUtilities
from data_printing import DataPrinting

def file_extract(directory, year):
    parser = FileParser(directory, year)
    records = parser.parse_files()

    max_temp = min_temp = max_humidity = None
    max_temp_day = min_temp_day = max_humidity_day = ""

    for record in records:
        if max_temp is None or record.max_temp > max_temp:
            max_temp = record.max_temp
            max_temp_day = DateUtilities.format_date(record.date)

        if min_temp is None or record.min_temp < min_temp:
            min_temp = record.min_temp
            min_temp_day = DateUtilities.format_date(record.date)

        if max_humidity is None or record.max_humidity > max_humidity:
            max_humidity = record.max_humidity
            max_humidity_day = DateUtilities.format_date(record.date)

    return max_temp, max_temp_day, min_temp, min_temp_day, max_humidity, max_humidity_day

def main():
    if len(sys.argv) != 4 or sys.argv[2] != "-e":
        print("Usage: weatherman.py /path/to/files-dir -e year")
        return

    directory = sys.argv[1]
    year = sys.argv[3]

    max_temp, max_temp_day, min_temp, min_temp_day, max_humidity, max_humidity_day = file_extract(directory, year)

    DataPrinting.print_weather_report(max_temp, max_temp_day, min_temp, min_temp_day, max_humidity, max_humidity_day)

if __name__ == "__main__":
    main()
