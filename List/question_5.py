first_set = {23, 42, 65, 57, 78, 83, 29}
second_set = {57, 83, 29, 67, 73, 43, 48}

for x in first_set & second_set:
    first_set.remove(x)

print(first_set)