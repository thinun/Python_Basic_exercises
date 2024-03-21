user_input = input("Enter your name: ")
if user_input.isalpha():
    x = 0
    for x in range(len(user_input)):
        if x % 2 == 0:
            print(user_input[x])

    else:
        print("please enter your name")
