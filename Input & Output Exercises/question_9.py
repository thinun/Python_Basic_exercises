with open('txt_3.txt', 'r') as user:
    new_user = user.read()
    if new_user == '':
        print('file is empty')
    else:
        print('file is not empty')

