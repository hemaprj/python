class Vehicle():
    def general_usage(self) :
        print("General Usage is transportation")

class Car(Vehicle):
    def __init__(self):
        self.roof="has"
        self.tyres=4
        self.general_usage()
        print(f"My car has  {self.tyres} tyres and {self.roof} roof")

class MotorCycle(Vehicle):
    def __init__(self):
        self.roof="does not have"
        self.tyres=2
        self.general_usage()
        print(f"My motorcycle has  {self.tyres} tyres and {self.roof} roof")

c=Car()
m=MotorCycle()

print(isinstance(c,Car))
print(isinstance(m,Car))
print(issubclass(Car,MotorCycle))
print(issubclass(MotorCycle,Vehicle ))