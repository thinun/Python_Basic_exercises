for x in range(1, 11):
    print(x * 1, end=' ')
    print(x * 2, end=' ')
    print(x * 3, end=' ')
    print(x * 4, end=' ')
    print(x * 5, end=' ')
    print(x * 6, end=' ')
    print(x * 7, end=' ')
    print(x * 8, end=' ')
    print(x * 9, end=' ')
    print(x * 10)

# another way

for x in range(1, 11):
    for i in range(1, 11):
        print(x * i, end=' ')

    print('\t')
