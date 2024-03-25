str1 = "Thinun29@#8496"
avg = 0
addition = 0
count_of_numbers = 0
for x in str1:
    if x.isnumeric():
        addition = addition + int(x)
        count_of_numbers = count_of_numbers + 1
        avg = addition / count_of_numbers

    else:
        pass
print(f'The average of {addition} is {avg:.2f}')
