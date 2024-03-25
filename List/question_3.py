sample_list = [11, 45, 8, 11, 23, 45, 23, 45, 89]

dict ={}

for i in sample_list:

    dict[i] = sample_list.count(i)


print(dict)