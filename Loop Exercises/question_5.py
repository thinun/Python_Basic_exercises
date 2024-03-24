numbers = [12, 75, 150, 180, 145, 525, 50]
new_list = []
for number in numbers:
    if number > 500:
        break
    elif number % 5 == 0 and number <= 150:
        new_list.append(number)

print(new_list)
