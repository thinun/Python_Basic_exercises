def user_income():
    try:
        user_input = int(input("Enter your Income: "))
        return user_input

    except ValueError:
        return "Please enter your income in numbers!"




def tax_cal(user_input):
    if user_input <= 10000:
        tax = user_input * 0
        return tax
    elif 10000 < user_input <= 20000:
        tax = (user_input - 10000) * 10 / 100
        return tax
    elif user_input >= 20000:
        tax = ((user_input - 20000) * 20 / 100) + (10000 * 10 / 100)
        return tax
    else:
        return "invalid input"


if __name__ == "__main__":
    user_tax = user_income()
    user_tax = tax_cal(user_tax)
    print(f'your monthly tax is:', user_tax)
