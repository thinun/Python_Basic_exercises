my_list = [50, 6, 7, 80, 10, 'thinun']
try:
    for i in my_list:

        if i % 5 == 0:
            print(i)
        else:
            pass
except TypeError:
    print(f"Please make sure to have only numbers in the list")
