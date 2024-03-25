str1 = "Apple"
dict = {}

for x in str1:
    dict.update({x: str1.count(x)})

print(dict)