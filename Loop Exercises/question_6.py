try:
    user_input = int(input("Enter a number: "))
    new_num = str(user_input)
    print(f'length of the number is: {len(new_num)} ')
except ValueError:
    print("Invalid input")


