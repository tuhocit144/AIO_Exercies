from abc import ABC, abstractmethod


class Product (ABC):
    def __init__(self, name, price, manufacture, inventory_quality):
        self._name = name
        self._price = price
        self._manufacture = manufacture
        self._inventory_quality = inventory_quality
    # hien thuc 2 phuong thuc __eq__ va __hash__ de kiem tra hai san pham ko duoc trung ten

    def __eq__(self, other):
        if isinstance(other, Product):
            return self._name == other._name
        return False

    def __hash__(self):
        return hash(self._name)

    def __str__(self):
        info = '| {} | {} | {} | {} |'.format(
            self._name, self._price, self._manufacture, self._inventory_quality)
        return info

    @abstractmethod
    def describe(self):
        pass

    def get_name(self):
        return self._name

    def set_name(self, name):
        self._name = name

    def get_price(self):
        return self._price

    def set_price(self, price):
        if price < 0:
            print('Price must be granter than or equal zero')
        else:
            self._price = price

    def get_manufacture(self):
        return self._manufacture

    def set_manufacture(self, manufacture):
        if manufacture is None:
            print('Manufacture must have value')
        else:
            self._manufacture = manufacture

    def get_inventory_quality(self):
        return self._inventory_quality

    def set_inventory_quality(self, quality):
        if quality < 0:
            print('inventory_quality must be greater than or equal zero')
        else:
            self._inventory_quality = quality


class Phone(Product):
    def __init__(self, name, price, manufacture, inventory_quality, opr_system, camera, ram, color):
        super().__init__(name, price, manufacture, inventory_quality)
        self.__opr_system = opr_system
        self.__camera = camera
        self.__ram = ram
        self.__color = color

    def get_opr_system(self):
        return self._opr_system

    def set_opr_system(self, opr_system):
        self._opr_system = opr_system

    def get_camera(self):
        return self._camera

    def set_camera(self, camera):
        self._camera = camera

    def get_ram(self):
        return self._ram

    def set_ram(self, ram):
        self._ram = ram

    def get_color(self):
        return self._color

    def set_color(self, color):
        self._color = color

    def describe(self):
        info = super().__str__()
        info = info + ' {} | {} | {} | {} |'.format(
            self.__opr_system, self.__camera, self.__ram, self.__color)
        print(info, end=' ')

# class Laptop


class Laptop(Product):
    def __init__(self, name, price, manufacture, inventory_quality, display, opr_system, ram, internal_storage, processor):
        super().__init__(name, price, manufacture, inventory_quality)
        self.__opr_system = opr_system
        self.__ram = ram
        self.__internal_storage = internal_storage
        self.__processor = processor
        self.__display = display

    def get_display(self):
        return self.__display

    def set_display(self, display):
        self.__display = display

    def get_opr_system(self):
        return self.__opr_system

    def set_opr_system(self, opr_system):
        self.__opr_system = opr_system

    def get_ram(self):
        return self.__ram

    def set_ram(self, ram):
        self.__ram = ram

    def get_internal_storage(self):
        return self.__internal_storage

    def set_internal_storage(self, internal_storage):
        self.__internal_storage = internal_storage

    def get_processor(self):
        return self.__processor

    def set_processor(self, processor):
        self.__processor = processor
    # implement descibe

    def describe(self):
        info = super().__str__()
        info = info + ' {} | {} | {} | {} | {} |'.format(
            self.__display, self.__ram, self.__opr_system, self.__processor, self.__internal_storage)
        print(info, end=' ')

# class TV


class TV(Product):
    def __init__(self, name, price, manufacture, inventory_quality, screen_size, resolution, display_tech, opr_system):
        super().__init__(name, price, manufacture, inventory_quality)
        self.__screen_size = screen_size
        self.__resolution = resolution
        self.__display_tech = display_tech
        self.__opr_system = opr_system

    def get_screen_size(self):
        return self.__screen_size

    def set_screen_size(self, screen_size):
        self.__screen_size = screen_size

    def get_resolution(self):
        return self.__resolution

    def set_resolution(self, resolution):
        self.__resolution = resolution

    def get_display_tech(self):
        return self.__display_tech

    def set_display_tech(self, display_tech):
        self.__display_tech = display_tech

    def get_opr_system(self):
        return self.__opr_system

    def set_opr_system(self, opr_system):
        self.__opr_system = opr_system

    def describe(self):
        info = super().__str__()
        info = info + ' {} | {} | {} | {} |'.format(
            self.__screen_size, self.__resolution, self.__display_tech, self.__opr_system)
        print(info, end=' ')

# class Custommer


class Custommer:
    def __init__(self, id_cus, full_name, cus_phone):
        self.__id_cus = id_cus
        self.__full_name = full_name
        self.__cus_phone = cus_phone

    def get_id_cus(self):
        return self.__id_cus

    def set_id_cus(self, id_cus):
        self.__id_cus = id_cus

    def get_full_name(self):
        return self.__full_name

    def set_full_name(self, full_name):
        self.__full_name = full_name

    def get_cus_phone(self):
        return self.__cus_phone

    def set_cus_phone(self, cus_phone):
        self.__cus_phone = cus_phone


class Order(Custommer):
    def __init__(self, id_cus, full_name, cus_phone):
        super().__init__(id_cus, full_name, cus_phone)
        self.__products = {}

    def add_product(self, product, quality):
        # kiem tra xem san pham nay co trong hoa don hay chua, neu co thi cong don so luong
        if product in self.__products:
            self.__products[product] += quality
        else:
            self.__products[product] = quality

    def get_products(self):
        return self.__products

    def caculate_total_price(self):
        total_value = 0
        for pro, key in self.__products.items():
            total_value += pro.get_price() * key
        return total_value

    def show_list_product(self):
        for pro, key in self.__products.items():
            pro.describe()
            print(f' | quality:  {key}|')


# test
p1 = Phone('IP14', 27500000, 'Apple', 10, 'IOS', 'Camera 15', 128, 'White')
laptop1 = Laptop('Dell', 17500000, 'Dell', 25, 15, 'Windows', 16, 512, 'Intel')
tv1 = TV('Samsung 51AO1', 11500000, 'Sam Sung',
         5, 50, 'Full HD', 'LCD', 'Android 4.0')
order = Order('k001', 'an khang', '1234566787')
order.add_product(p1, 2)
order.add_product(laptop1, 1)
order.add_product(tv1, 1)
laptop2 = Laptop('Dell', 17500000, 'Dell', 25, 15, 'Windows', 16, 512, 'Intel')
order.add_product(laptop2, 3)
print('*'*80)
print('Product list in order:')
order.show_list_product()
print('*'*80)
print('\tTotal of bill: {:,}'.format(order.caculate_total_price()))
print('*'*80)
