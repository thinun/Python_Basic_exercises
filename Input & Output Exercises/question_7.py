try:
    user_1, user_2, user_3 = input('Enter two numbers separated by space: ').split(' ')

    print(user_1)
    print(user_2)
    print(user_3)
except ValueError:
    print('Please enter 3 values')

