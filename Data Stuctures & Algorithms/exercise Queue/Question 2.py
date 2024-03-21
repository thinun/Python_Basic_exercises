from collections import deque


class Queue:
    def __init__(self):
        self.queue = deque()

    def enqueue(self, data):
        self.queue.appendleft(data)

    def dequeue(self):
        if len(self.queue) == 0:
            return print("Queue is empty")
        else:
            return self.queue.pop()

    def isEmpty(self):
        return len(self.queue) == 0

    def size(self):
        return len(self.queue)

    def front(self):
        if len(self.queue) == 0:
            print("Queue is empty")
        return self.queue[-1]


obj1 = Queue()


def binary(n):
    obj1.enqueue('1')
    for i in range(n):
        front = obj1.front()
        print('', front)
        obj1.enqueue(front + "0")
        obj1.enqueue(front + "1")
        obj1.dequeue()



binary(10)
