def string_remove(user_input, n):
    if user_input.isalpha():
        print(user_input[n:])
        return user_input


string_remove(user_input='thinun', n=2)
