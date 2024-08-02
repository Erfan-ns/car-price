class Car:
    def __init__(self, x, y):
        self.name = x
        self.price = y
        print(f"{self.name} costs {self.price}")


c1 = Car("benz", 900)
c2 = Car("pride", 100)
