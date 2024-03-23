user_input = int(input("Enter a number: "))
new_list = []
for i in range(1, user_input + 1):
    new_list.append(i)

print(f'Sum of all the numbers from 1 to {user_input} is:', sum(new_list))
