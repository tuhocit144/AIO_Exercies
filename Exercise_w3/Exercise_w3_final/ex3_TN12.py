class MyQueue:
    def __init__(self, capacity=5):
        self.__queue = []
        self.__capacity = capacity

    def is_empty(self):
        return (len(self.__queue) == 0)

    def is_full(self):
        return (len(self.__queue) == self.__capacity)

    def dequeue(self):
        if (self.is_empty()):
            return 'Queue is empty. Do not thing'
        return self.__data.pop(0)

    def enqueue(self, x):
        if (self.is_full()):
            return 'Queue is full. Do not thing'
        self.__queue.append(x)

    def front(self):
        if (self.is_empty()):
            return 'Queue is empty. Do not thing'
        return self.__queue[0]


queue1 = MyQueue(capacity=5)
queue1 . enqueue(1)
assert queue1 . is_full() == False
queue1 . enqueue(2)
print(queue1.front())
