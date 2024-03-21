user_input = input("Enter a number: ")

if user_input == user_input[::-1]:
    print('The number is palindrome')
else:
    print('The number is not palindrome')
