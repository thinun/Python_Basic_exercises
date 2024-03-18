file = open('nyc_weather.csv', 'r')
my_dict = {}
for line in file:
    data = line.strip().split(',')
    date = data[0]
    temp = data[1]
    my_dict[date] = temp
user_input = input("enter the date like this ex: Jan 4 : ")
try:
    print(my_dict[user_input], 'F')
except KeyError:
    print("Sorry wrong date")
