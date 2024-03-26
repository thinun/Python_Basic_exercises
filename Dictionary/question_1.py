keys = ['Ten', 'Twenty', 'Thirty']
values = [10, 20, 30]
dictionary = dict(zip(keys, values))
print(dictionary)

# another way
new_dict = {}
for i in range(len(keys)):
    new_dict[keys[i]] = values[i]

print(new_dict)
