class Person():
    def __init__(self, name, phone):
        self._name = name
        self._phone = phone

    def describe(self):
        return ('Name: {}, phone: {}').format(self._name, self._phone)

    def __eq__(self, other):
        if isinstance(other, Person):
            return self._phone == other._phone
        return False

    def __hash__(self):
        return hash(self.phone)


class Employee(Person):
    def __init__(self, name, phone, annual_salary, year_of_starting_work):
        super().__init__(name, phone)
        self.__annual_salary = annual_salary
        self.__year_of_starting_work = year_of_starting_work

    def describe(self):
        info = 'Employee: ' + super().describe()
        info = info + (' annual_salary: {}, year_of_starting_work: {}').format(
            self.__annual_salary, self.__year_of_starting_work)
        return info


class StackEmployee():
    def __init__(self, capacity=5):
        self.__capacity = capacity
        self.__employees = []

    def is_full(self):
        return len(self.__employees) == self.__capacity

    def is_empty(self):
        return len(self.__employees) == 0

    def pop(self):
        return self.__employees.pop(-1)

    def push(self, obj):
        if self.is_full():
            print('Stack is full. Do not push obj')
        elif self.__employees.__contains__(obj):
            print('This obj have same phone with another in stack. Do not push obj')
        else:
            self.__employees.append(obj)

    def top(self):
        if self.is_empty():
            print('Stack is empty. No element in stack')
        else:
            return self.__employees[-1]

    def describe(self):
        for x in self.__employees:
            print(x.describe())


# test
stack_employee = StackEmployee()
employee1 = Employee('An', '0912345678', 250, 2002)
employee2 = Employee('Binh', '0912225678', 500, 2001)
employee3 = Employee('Nghia', '0912225678', 350, 2002)
employee4 = Employee('Tin', '0912335678', 700, 2000)
employee5 = Employee('Tai', '0914445678', 850, 2003)
employee6 = Employee('Binh', '0955225678', 900, 2004)
employee7 = Employee('Binh', '0956225678', 800, 2002)
# push to stack
stack_employee.push(employee1)
stack_employee.push(employee2)
stack_employee.push(employee3)
stack_employee.push(employee4)
stack_employee.push(employee5)
stack_employee.push(employee6)
stack_employee.push(employee7)
# print stack
print('-'*70)
print('List element of stack after push 6 element is: ')
stack_employee.describe()
# pop
obj = stack_employee.pop()
print('-'*70)
print('Element on top of stack is: \n   ', obj.describe())
print('-'*70)
print('List element of stack after pop element is: ')
stack_employee.describe()
# top
obj = stack_employee.top()
print('-'*70)
print('Element on top of stack is: \n', obj.describe())
print('List element of stack is: ')
stack_employee.describe()
