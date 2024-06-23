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


class Doctor(Person):
    def __init__(self, name, yob, specialist):
        super().__init__(name, yob)
        self.__specialist = specialist

    def describe(self):
        print(f'Doctor - {super().__str__()}, specialist: {self.__specialist}')

doctor1 = Doctor ( name =" doctorZ2023 ", yob =1981 , specialist =" Endocrinologists ")
assert doctor1 . _yob == 1981
doctor1 . describe ()
