number = 7536
print("Given number", number)

reversed_number = 0
while number > 0:
    # get the last digit
    digit = number % 10
    # append the digit to the reversed number
    reversed_number = (reversed_number * 10) + digit
    # remove the last digit and repeat the loop
    number = number // 10

print("Reversed number:", reversed_number)
