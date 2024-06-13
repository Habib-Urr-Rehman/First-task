# weatherman.py
import sys
from file_parser import FileParser
from data_printing import print_averages
from date_utilities import parse_year_month

def calculate_averages(records):
    if not records:
        return None, None, None

    total_max_temp = sum(record.max_temp for record in records)
    total_min_temp = sum(record.min_temp for record in records)
    total_mean_humidity = sum(record.mean_humidity for record in records)

    count = len(records)

    avg_max_temp = total_max_temp / count
    avg_min_temp = total_min_temp / count
    avg_mean_humidity = total_mean_humidity / count

    return avg_max_temp, avg_min_temp, avg_mean_humidity

def main():
    if len(sys.argv) != 4 or sys.argv[2] != "-a":
        print("Usage: weatherman.py /path/to/files-dir -a year/month")
        return

    directory = sys.argv[1]
    year_month = sys.argv[3]
    try:
        year, month = parse_year_month(year_month)
    except ValueError as e:
        print(e)
        return

    parser = FileParser(directory)
    records = parser.parse_files(year, month)
    avg_max_temp, avg_min_temp, avg_mean_humidity = calculate_averages(records)
    print_averages(avg_max_temp, avg_min_temp, avg_mean_humidity, year, month)

if __name__ == "__main__":
    main()
