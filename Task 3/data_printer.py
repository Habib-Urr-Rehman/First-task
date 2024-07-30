def print_weather_report(records):
    for record in records:
        max_bar = '+' * record.max_temp
        min_bar = '+' * record.min_temp
        print(f"{record.date.day:02d} \033[91m{max_bar}\033[0m {record.max_temp}C")  # 1.Reference  https://stackoverflow.com/questions/15580303/python-output-complex-line-with-floats-colored-by-value
        print(f"{record.date.day:02d} \033[94m{min_bar}\033[0m {record.min_temp}C")
