set1 = {10, 20, 30, 40, 50}
set2 = {30, 40, 50, 60, 70}

set3 = set1.intersection(set2)
print(set3)
set4 = set1.union(set2)
print(set4)

set5 = set4.difference(set3)
print(set5)

#another way

set6 = set1.symmetric_difference(set2)
print(set6)
