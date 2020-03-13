# To the GroundVehicle class, add method drive() that returns "vroooom".
#
# Also change it so the num_wheels defaults to 4 if not specified when the
# object is constructed.

class GroundVehicle():
    def __init__(self, num_wheels=4):
        self.num_wheels = num_wheels

    # TODO
    def drive(self):
        print("vroooom")
        print(f"Wheels: {self.num_wheels}")

# Subclass Motorcycle from GroundVehicle.
#
# Make it so when you instantiate a Motorcycle, it automatically sets the number
# of wheels to 2 by passing that to the constructor of its superclass.
#
# Override the drive() method in Motorcycle so that it returns "BRAAAP!!"

# TODO
class Motorcycle(GroundVehicle):
    def __init__(self):
        super().__init__(num_wheels=2)
        
    def drive(self):
        print("BRAAAP!!")
        print(f"Wheels: {self.num_wheels}")

vehicles = [
    GroundVehicle(),
    GroundVehicle(),
    Motorcycle(),
    GroundVehicle(),
    Motorcycle(),
]

# Go through the vehicles list and print the result of calling drive() on each.

# TODO

# test1 = Motorcycle()
# print(f"test {test1.drive()}")

for i in vehicles:
    print(i.drive())