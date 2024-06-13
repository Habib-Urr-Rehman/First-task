def generate_bar_chart(data):
    for day, temps in sorted(data.items()):
        max_temps = [temp[0] for temp in temps]
        min_temps = [temp[1] for temp in temps]
        max_temp = sum(max_temps) / len(max_temps)
        min_temp = sum(min_temps) / len(min_temps)
        max_bar = '+' * round(max_temp)
        min_bar = '+' * round(min_temp)
        print(f"{day:02d} \033[91m{max_bar}\033[0m {max_temp:.1f}C")
        print(f"{day:02d} \033[94m{min_bar}\033[0m {min_temp:.1f}C")
