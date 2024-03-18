# question 1

file = open("nyc_weather.csv", "r")
weather_data = []
for line in file:
    # print(line)
    data = line.strip().split(',')
    try:
        temp = int(data[1])
        weather_data.append(temp)
    except ValueError:
        continue

print(weather_data)

seven_days_temperature = sum(weather_data[:7]) / 7
print(seven_days_temperature)
max_tem_in_ten_days = max(weather_data[:10])
print(max_tem_in_ten_days)
