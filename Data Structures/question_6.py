first_set = {27, 43, 34}
second_set = {34, 93, 22, 27, 43, 53, 48}

if first_set <= second_set:
    print("The first is a sub set of the second")
    print(first_set.clear())
    print(second_set)
elif second_set <= first_set:
    print("The second is a sub set of the first")
    print(first_set)
    print(second_set.clear())
else:
    print("invalid")
