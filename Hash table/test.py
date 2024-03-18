file = open("nyc_weather.csv", "r")
weather_data = {}
for line in file:
    data = line.strip().split(',')
    date = data[0]
    temperature = data[1]
    weather_data[date] = temperature

print(weather_data)

start_date = 'Jan 1'
end_date = 'Jan 7'

day_weather = {date: weather_data[date] for date in weather_data if start_date <= date <= end_date}
print(day_weather)

file.close()
