def middle_string(str1):
    return [str1[((len(str1) - 1) // 2) - 1], str1[(len(str1) - 1) // 2], str1[((len(str1) - 1) // 2) + 1]]


str2 = middle_string("thinun")

for x in str2:
    print(x, end='')
