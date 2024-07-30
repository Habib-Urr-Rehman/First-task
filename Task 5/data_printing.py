# data_printing.py

def generate_bar_chart(data):
    for day, temps in sorted(data.items()):
        max_temps = [temp[0] for temp in temps]
        min_temps = [temp[1] for temp in temps]
        max_temp = max(max_temps)
        min_temp = min(min_temps)
        max_bar = '+' * max_temp
        min_bar = '+' * min_temp
        print(f"{day:02d} \033[91m{min_bar}\033[0m \033[94m{max_bar}\033[0m {min_temp}C - {max_temp}C")
