class Car:
    def __init__(self, mark, fuel_type, engine_volume, kpp, rashod):
        self.car_mark = mark
        self.p_type = fuel_type
        self.engine_v = engine_volume
        self.kpp = kpp
        self.fuel_state = 100
        self.rashod = rashod

    def get_attrs(self):
        print(self.car_mark)
        print(self.p_type)
        print(self.engine_v)
        print(self.kpp)

    def get_s(self):
        s = self.fuel_state / self.rashod
        return s



car_1 = Car("bmw", "petrol", 3.0, "auto", 9.2)
s = car_1.get_s()
print(s)