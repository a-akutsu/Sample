class Car:
    def accel(self):
        print("最高速度180km")

class sports(Car):
    def accel(self):
        print("最高速度420km")

car = sports()
car.accel()