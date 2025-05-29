from laptop.validator import laptop_validator


class Laptop:
    def __init__(self, brand, ram, cpu, screensize, man_date, price):
        self.brand = brand
        self.ram = ram
        self.cpu = cpu
        self.screensize = screensize
        self.man_date = man_date
        self.price = price

    def save_laptop(self):
        print(f"{self.brand}-{self.ram}-{self.cpu}-{self.screensize}-{self.man_date}-{self.price}saved")

    def Validate(self):
        return laptop_validator(self)
