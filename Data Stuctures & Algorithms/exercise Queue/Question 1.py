import time
import threading
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
        else:
            return self.queue.pop()

    def is_empty(self):
        return len(self.queue) == 0

    def size(self):
        return len(self)


def placing_order(order):
    for x in order:
        person_one.enqueue(x)
        print("placing order for ", x)
        time.sleep(0.5)


def serving_order():
    time.sleep(1)
    while True:
        serve = person_one.dequeue()
        if len(person_one.queue) == 0:
            print('order is empty')
            break
        else:
            print('serving order ', serve)
            time.sleep(2)


person_one = Queue()
if __name__ == "__main__":
    order = ['pizza', 'samosa', 'pasta', 'biryani', 'burger']
    t1 = threading.Thread(target=placing_order, args=(order,))
    t2 = threading.Thread(target=serving_order, args=())
    t1.start()
    t2.start()
    t1.join()
    t2.join()
    end_time = time.time()
    print("time: {}".format(end_time - start_time))
