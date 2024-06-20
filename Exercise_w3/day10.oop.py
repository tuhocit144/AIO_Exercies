# define class Staff
class Staff:
    def __init__(self, name, age, address, salary, total_time):
        self.__name = name
        self.__age = age
        self.__address = address
        self.__salary = salary
        self.__total_time = total_time

    def show_info(self):
        print(f'Name: {self.__name}, age: {self.__age}', end=' ')
        print(f'address: {self.__address}, salary: {self.__salary}')
        print(f'\t\ttoatal_time: {self.__total_time}, bonus: ', end=' ')
        print(f'{self.calculate_bonus()}')

    def calculate_bonus(self):
        bonus = 0
        if self.__total_time >= 200:
            bonus = self.__salary*0.2
        elif self.__total_time >= 100:
            bonus = self.__salary*0.1
        return bonus


# test
staff1 = Staff('An', 25, 'Q10_TPHCM', 30000000, 300)
staff2 = Staff('Bình', 28, 'Q2_TPHCM', 50000000, 199)
staff3 = Staff('Nga', 29, 'Q.Bình Thạnh', 10000000, 99)
# output
staff1.show_info()
staff2.show_info()
staff3.show_info()
