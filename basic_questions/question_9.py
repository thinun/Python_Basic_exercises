list1 = [10, 20, 25, 30, 35]
list2 = [40, 45, 60, 75, 90]
my_list = []
for i in list2:
    if i % 2 == 0:
        my_list.append(i)

for x in list1:
    if x % 2 != 0:
        my_list.append(x)
sorted_list = sorted(my_list)
print(sorted_list)
