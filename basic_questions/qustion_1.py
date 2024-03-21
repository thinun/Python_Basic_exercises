previous_number = 0

for number in range(1, 11):
    print(
        f"current number is:{number} previous number is:{previous_number} Sum of the numbers is: {previous_number + number}")
    previous_number = previous_number + 1
