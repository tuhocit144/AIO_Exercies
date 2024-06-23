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


class Student(Person):
    def __init__(self, name, yob, grade):
        super().__init__(name, yob)
        self.__grade = grade

    def describe(self):
        print(f'Student - {super().__str__()}, grade: {self.__grade}')


# test
student1 = Student(name=" studentZ2023 ", yob=2011, grade="6")
assert student1._yob == 2011
student1.describe()
