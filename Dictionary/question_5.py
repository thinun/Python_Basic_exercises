sample_dict = {
    "name": "Kelly",
    "age": 25,
    "salary": 8000,
    "city": "New york"}
new_dict = {}

for key in sample_dict:
    if key == 'name':
        new_dict[key] = sample_dict[key]
    elif key == 'salary':
        new_dict[key] = sample_dict[key]
    else:
        pass

print(new_dict)
