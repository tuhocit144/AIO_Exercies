class MyQueue:
    def __init__(self, capacity=5):
        self.__queue = []
        self.__capacity = capacity

    def is_empty(self):
        return (len(self.__queue) == 0)

    def is_full(self):
        return (len(self.__queue) == self.__capacity)

    def describe(self):
        print(self.__queue)

    def enqueue(self, x):
        if (self.is_full()):
            return 'Queue is full. Do not thing'
        self.__queue.append(x)

    def dequeue(self):
        if (self.is_empty()):
            return 'Queue is empty. Do not thing'
        return self.__queue.pop(0)

    def front(self):
        if (self.is_empty()):
            return 'Queue is empty. Do not thing'
        return self.__queue[0]


# test
queue1 = MyQueue(capacity=5)

queue1.enqueue(1)
queue1.enqueue(2)
print(queue1.is_full())
print(queue1.front())
print(queue1.dequeue())
print(queue1.front())
print(queue1.dequeue())
print(queue1.is_empty())
