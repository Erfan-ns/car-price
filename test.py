
class Car:
    def __init__(self, x, y):
        self.name = x
        self.price = y

    def show(self):
        print(f"{self.name} costs {self.price}")


c1 = Car("benz", 900)
c2 = Car("pride", 100)

c1.show() 
c2.show()
