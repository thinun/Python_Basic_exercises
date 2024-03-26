sample_list = [11, 45, 8, 23, 14, 12, 78, 45, 89]

chunk = len(sample_list) // 3
print('1st chunk', sample_list[:chunk])
print('2nd chunk', sample_list[chunk:-chunk])
print('3rd chunk', sample_list[-chunk:])
