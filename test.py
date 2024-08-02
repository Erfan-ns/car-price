class CAR:
    wheel = 4
    obj_nums = 0

    def __init__(self, x, y):
        self.name = x
        self.price = y
        print(f"{self.name} costs {self.price} and has got {CAR.wheel} wheels")
        CAR.obj_nums += 1


c1 = CAR("benz", 900)
c2 = CAR("pride", 100)

print(f"car count : {CAR.obj_nums}")
