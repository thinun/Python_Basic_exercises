employees = ['Kelly', 'Emma']
defaults = {"designation": 'Developer', "salary": 8000}

new_dict = {}

for key in employees:
    new_dict[key] = defaults

print(new_dict)
