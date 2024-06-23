from abc import ABC, abstractmethod


class Person(ABC):
    def __init__(self, name, yob):
        self._name = name
        self._yob = yob

    def __str__(self):
        return 'Name: {}, yob: {}'.format(self._name, self._yob)

    @abstractmethod
    def describe(self):
        pass

    def get_yob(self):
        return self._yob


class Teacher(Person):
    def __init__(self, name, yob, subject):
        super().__init__(name, yob)
        self.__subject = subject

    def describe(self):
        print(f'Teacher - {super().__str__()}, subject: {self.__subject}')


teacher1 = Teacher(name=" teacherZ2023 ", yob=1991, subject=" History ")
assert teacher1 . _yob == 1991
teacher1 . describe()