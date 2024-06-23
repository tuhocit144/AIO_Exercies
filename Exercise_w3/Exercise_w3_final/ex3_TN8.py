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


class Student(Person):
    def __init__(self, name, yob, grade):
        super().__init__(name, yob)
        self.__grade = grade

    def describe(self):
        print(f'Student - {super().__str__()}, grade: {self.__grade}')


class Teacher(Person):
    def __init__(self, name, yob, subject):
        super().__init__(name, yob)
        self.__subject = subject

    def describe(self):
        print(f'Teacher - {super().__str__()}, subject: {self.__subject}')


class Ward:
    def __init__(self, name):
        self.__lst_person = []
        self.__name = name

    def add_person(self, person: Person):
        self.__lst_person.append(person)

    def describe(self):
        print(f'Ward: {self.__name}, có các person sau:')
        for x in self.__lst_person:
            x.describe()

    def __call__(self, name):
        self.__name = name

    def count_doctor(self):
        count = 0
        for x in self.__lst_person:
            if type(x) is Doctor:
                count += 1
        return count

    def get_name(self):
        return self.__name
    # sort theo tuoi

    def sort_age(self):
        self.__lst_person.sort(key=lambda x: x._yob)

    def compute_average(self):
        sum_age = sum(item._yob for item in self.__lst_person)
        return sum_age/len(self.__lst_person)


# main
student1 = Student(name=" studentA ", yob=2010, grade="7")
teacher1 = Teacher(name=" teacherA ", yob=1969, subject=" Math ")
teacher2 = Teacher(name=" teacherB ", yob=1995, subject=" History ")
doctor1 = Doctor(name=" doctorA ", yob=1945, specialist=" Endocrinologists ")
doctor2 = Doctor(name=" doctorB ", yob=1975, specialist=" Cardiologists ")
ward1 = Ward(name=" Ward1 ")
ward1.add_person(student1)
ward1.add_person(teacher1)
ward1.add_person(teacher2)
ward1.add_person(doctor1)
assert ward1 . count_doctor() == 1
ward1.add_person(doctor2)
print(ward1 . count_doctor())
