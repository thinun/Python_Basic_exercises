s1 = "Ault"
s2 = "Kelly"

new_string_1 = []

for x in s1:
    new_string_1.append(x)

new_string_1.insert(len(new_string_1) // 2, s2)

for j in new_string_1:
    print(j, end='')
