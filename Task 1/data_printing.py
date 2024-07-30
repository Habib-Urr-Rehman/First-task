class DataPrinting:
    @staticmethod
    def print_weather_report(max_temp, max_temp_day, min_temp, min_temp_day, max_humidity, max_humidity_day):
        print(f"Highest: {max_temp}C on {max_temp_day}")
        print(f"Lowest: {min_temp}C on {min_temp_day}")
        print(f"Humidity: {max_humidity}% on {max_humidity_day}")
