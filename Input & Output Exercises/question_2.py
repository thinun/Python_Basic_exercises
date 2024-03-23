user_name = input("Enter your name: ")
if user_name.replace(' ', '').isalpha():
    new_name = user_name.replace(' ', '*')
    print('your new name is ' + new_name)
else:
    print('Enter your name correctly!')
