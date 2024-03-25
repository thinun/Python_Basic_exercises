str1 = "James"
new_string = [str1[len(str1) - len(str1)], str1[(len(str1) - 1) // 2], str1[len(str1) - 1]]

for x in new_string:
    print(x, end='')
