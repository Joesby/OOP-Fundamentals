#define a new Vehicle class with variables for register number, type, and owner
class Vehicle:
    def __init__(self, reg_num, type, owner):
        self.registration_number = reg_num
        self.type = type
        self.owner = owner

    #add a method for updating the owner of the vehicle object
    def update_owner(self, new_owner):
        self.owner = new_owner

#create objects of the Vehicle class, each with unique attributes
corolla = Vehicle(1, "sedan", "Bill")
carnival = Vehicle(2, "van", "Gary")
harley = Vehicle(3, "motorcycle", "Leo")

#display the owners of each Vehicle object
print(corolla.owner)
print(carnival.owner)
print(harley.owner)
print()

#alter the owners of each object
corolla.update_owner("Amanda")
carnival.update_owner("Steve")
harley.update_owner("Joe")

#display the new owners of each vehicle object
print(corolla.owner)
print(carnival.owner)
print(harley.owner)