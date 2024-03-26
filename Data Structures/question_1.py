l1 = [3, 6, 9, 12, 15, 18, 21]
l2 = [4, 8, 12, 16, 20, 24, 28]
l3 = []
for x in range(len(l1)):
    if x % 2 != 0:

        l3.append(l1[x])
    else:

        l3.append(l2[x])

print(l3)
