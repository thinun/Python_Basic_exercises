roll_number = [47, 64, 69, 37, 76, 83, 95, 97]
sample_dict = {'Jhon': 47, 'Emma': 69, 'Kelly': 76, 'Jason': 97}


for x in roll_number:
    if x not in sample_dict.values():
        roll_number.remove(x)
    else:
        pass

print(roll_number)
print(sample_dict)