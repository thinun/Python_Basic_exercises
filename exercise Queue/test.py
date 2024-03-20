import time
from collections import deque

start_time = time.time()

class Queue:
    def __init__(self):
        self.queue = deque()

    def enqueue(self, order):
        self.queue.appendleft(order)

    def dequeue(self):
        if len(self.queue) == 0:
            print("order is empty")
            return None
        else:
            return self.queue.pop()

def placing_order(order):
    for item in order:
        person_one.enqueue(item)
        print("placing order for {}".format(item))
        time.sleep(0.5)

def serving_order():
    while True:
        served_item = person_one.dequeue()
        if served_item:
            print("serving order for {}".format(served_item))
            time.sleep(1)
        else:
            print("No orders left to serve")
            break

person_one = Queue()

if __name__ == "__main__":
    order = ['pizza', 'samosa', 'pasta', 'biryani', 'burger']

    placing_order(order)
    serving_order()

end_time = time.time()
print("time: {}".format(end_time - start_time))
