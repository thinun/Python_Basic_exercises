file = open('poem.txt', 'r')
my_dict = {}
for line in file:
    data = line.strip().split(' ')
    for x in data:
        my_dict[x] = my_dict.get(x, 0) + 1

print(my_dict)

for i in my_dict:
    print(i, my_dict[i])
