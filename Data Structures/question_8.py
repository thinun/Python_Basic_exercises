speed = {'jan': 47, 'feb': 52, 'march': 47, 'April': 44, 'May': 52, 'June': 53, 'july': 54, 'Aug': 44, 'Sept': 54}
my_list = []
my_set = set(speed.values())
for x in my_set:
    my_list.append(x)
print(my_list)