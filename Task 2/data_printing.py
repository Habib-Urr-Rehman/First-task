# data_printing.py
def print_averages(avg_max_temp, avg_min_temp, avg_mean_humidity, year, month):
    if avg_max_temp is None:
        print(f"No data available for {year}/{month}")
    else:
        print(f"Average Highest Temperature: {avg_max_temp:.1f}C")
        print(f"Average Lowest Temperature: {avg_min_temp:.1f}C")
        print(f"Average Mean Humidity: {avg_mean_humidity:.1f}%")
