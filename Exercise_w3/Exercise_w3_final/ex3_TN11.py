class MyQueue:
    def __init__(self, capacity=5):
        self.__queue = []
        self.__capacity = capacity

    def is_full(self):
        return (len(self.__queue) == self.__capacity)

    def enqueue(self, x):
        if (self.is_full()):
            return 'Queue is full. Do not thing'
        self.__queue.append(x)
    
queue1 = MyQueue ( capacity =5)
queue1 . enqueue (1)
assert queue1 . is_full () == False
queue1 . enqueue (2)
print ( queue1 . is_full ())
