def sum_of_number(number):
    x = 1
    addition = 0
    while x <= number:
        addition = addition + x
        x += 1

    return addition


print(sum_of_number(10))
