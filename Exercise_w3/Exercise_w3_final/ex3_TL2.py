from abc import ABC, abstractmethod


class Person(ABC):
    def __init__(self, name, yob):
        self._name = name
        self._yob = yob

    def __str__(self):
        return 'Name: {} - yob: {}'.format(self._name, self._yob)

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
        print(f'Doctor - {super().__str__()}', end=' ')
        print(f' - specialist: {self.__specialist}')


class Student(Person):
    def __init__(self, name, yob, grade):
        super().__init__(name, yob)
        self.__grade = grade

    def describe(self):
        print(f'Student - {super().__str__()} - grade: {self.__grade}')


class Teacher(Person):
    def __init__(self, name, yob, subject):
        super().__init__(name, yob)
        self.__subject = subject

    def describe(self):
        print(f'Teacher - {super().__str__()} - subject: {self.__subject}')


class Ward:
    def __init__(self, name):
        self.__lst_person = []
        self.__name = name

    def add_person(self, person):
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

    def compute_average_teacher(self):
        count_teacher = 0
        sum_age = 0
        for x in self.__lst_person:
            if isinstance(x, Teacher):
                count_teacher += 1
                sum_age += x.get_yob()
        if count_teacher > 0:
            return sum_age/count_teacher
        return None


# main
# (2a)
student1 = Student(name=" studentA ", yob=2010, grade="7")
student1.describe()
teacher1 = Teacher(name=" teacherA ", yob=1969, subject=" Math ")
teacher1.describe()
doctor1 = Doctor(name=" doctorA ", yob=1945, specialist=" Endocrinologists ")
doctor1.describe()
# (2b)
print()
teacher2 = Teacher(name=" teacherB ", yob=1995, subject=" History ")
doctor2 = Doctor(name=" doctorB ", yob=1975, specialist=" Cardiologists ")
# tao Ward
ward = Ward('HCM')
ward.add_person(student1)
ward.add_person(teacher1)
ward.add_person(teacher2)
ward.add_person(doctor1)
ward.add_person(doctor2)
ward.describe()
# in danh sách các doctor
print(f'Trong phố {ward.get_name()} có {ward.count_doctor()} bác sĩ')
print('Danh sach sau khi sap xep:')
ward.sort_age()
ward.describe()
print(f'Trung bình năm sinh của teacher trong quận ', end=' ')
print(f'{ward.get_name()} là: {ward.compute_average_teacher()}')
