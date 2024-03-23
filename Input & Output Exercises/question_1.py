try:
    user_one: int = int(input("Enter the 1st number: "))
    user_two: int = int(input("Enter the 2nd number: "))
    print('multiplication of these two numbers: ', user_one * user_two)

except ValueError:
    print("Invalid input")


