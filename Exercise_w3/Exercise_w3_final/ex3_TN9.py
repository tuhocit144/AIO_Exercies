class MyStack:
    def __init__(self, capacity=5):
        self.__stack = []
        self.__capacity = capacity

    def is_full(self):
        return (len(self.__stack) == self.__capacity)

    def push(self, value):
        if (self.is_full()):
            return 'Stack is full. Do not thing'
        self.__stack.append(value)


# test
stack1 = MyStack(capacity=5)
stack1 . push(1)
assert stack1 . is_full() == False
stack1 . push(2)
print(stack1 . is_full())
