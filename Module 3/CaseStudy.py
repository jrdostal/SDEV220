class Vehicle:
    type = ""

class Automobile(Vehicle):
    year = 2000
    make = ""
    model = ""
    doors = 2
    roof = "solid"

Car_1 = Automobile()

Car_1.type = input(print("Please enter the vehicle type: "))
Car_1.year = int(input(print("Please enter the vehicle year:")))    
Car_1.make = input(print("Please enter the vehicle make:"))  
Car_1.model = input(print("Please enter the vehicle model"))  
Car_1.doors = int(input(print("Please enter the number of doors:")))  
Car_1.roof = input(print("Please enter the style of roof"))             

print(f"\nCar_1 has the following information.\n")
print(f"Vehicle type: {Car_1.type}")
print(f"Year: {Car_1.year}")
print(f"Make: {Car_1.make}")
print(f"Model: {Car_1.model}")
print(f"Number of doors: {Car_1.doors}")
print(f"Type of roof: {Car_1.roof}\n")