class Car:
    def __init__(self, mark, fuel_type, engine_volume, kpp, rashod, probeg, year):
        self.car_mark = mark
        self.p_type = fuel_type
        self.engine_v = engine_volume
        self.kpp = kpp
        self.fuel_state = 100
        self.rashod = rashod
        self.probeg = probeg
        self.year = year

    def get_attrs(self):
        print(self.car_mark)
        print(self.p_type)
        print(self.engine_v)
        print(self.kpp)

    def get_s(self):
        s = self.fuel_state / self.rashod
        return s

    def need_fix(self):
        if self.probeg > 10000:
            return True
        else:
            return False



car_1 = Car("bmw", "petrol", 3.0, "auto", 9.2, 1000, 2008)
print(car_1.need_fix())