from collections import deque

stack = deque()
stack.append('hello sri lanka')
stack.append('my name is thinun')


def reverse():
    reversed_data = []
    for x in range(len(stack)):
        data = stack[x]
        new_data = data[::-1]
        reversed_data.append(new_data)
    return reversed_data


r_data = reverse()
for j in r_data:
    print(j)
