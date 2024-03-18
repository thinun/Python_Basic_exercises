from collections import deque

stack = deque()
stack.append('hello sri lanka')
stack.append('my name is thinun')
new_data = deque()
for x in stack:
    data = x.strip()
    print(data)
    i = 1
    while i <= len(data):
        new_data.append(data[-i])
        i += 1


result = ''.join(new_data)
print(result)
