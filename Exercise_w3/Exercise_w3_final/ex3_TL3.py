class MyStack:
    def __init__(self, capacity=5):
        self.__stack = []
        self.__capacity = capacity

    def is_empty(self):
        return (len(self.__stack) == 0)

    def is_full(self):
        return (len(self.__stack) == self.__capacity)

    def describe(self):
        print(self.__stack)

    def push(self, x):
        if (self.is_full()):
            return 'Stack is full. Do not thing'
        self.__stack.append(x)

    def pop(self):
        if (self.is_empty()):
            return 'Stack is empty. Do not thing'
        return self.__stack.pop(-1)

    def top(self):
        if (self.is_empty()):
            return 'Stack is empty. Do not thing'
        return self.__stack[-1]


# test
stack1 = MyStack()
stack1.push(1)
stack1.push(2)
print(stack1.is_full())
print(stack1.top())
print(stack1.pop())
print(stack1.top())
print(stack1.pop())
print(stack1.is_empty())
