num_list = []


def floating_num():
    i = 0
    while i < 3:
        try:
            user_input = float(input("Enter a floating number: "))
            num_list.append(user_input)
            i += 1
        except ValueError:
            print("Please enter only numbers!!!")


floating_num()
print(num_list)
