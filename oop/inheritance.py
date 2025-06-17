#Inheritance defines a class that inherits all the methods and properties from another class.

#parent class
class vericle:
    def __init__(self, brand, wheels):
        self.brand = brand
        self.wheels = wheels

    def show_info(self):
        print(f"Brand: {self.brand}, Wheels: {self.wheels}")


#child class
class car(vericle):
    def __init__(self, brand, wheels, fuel_type): #(The __init__() function is called automatically every time the class is being used to create a new object. When you add the __init__() function, the child class will no longer inherit the parent's __init__() function. To keep the inheritance of the parent's __init__() function, add a call to the parent's __init__() function:            
        super().__init__(brand, wheels) # Call parent constructor to set brand and wheels. By using the super() function, you do not have to use the name of the parent element, it will automatically inherit the methods and properties from its parent.
        self.fuel_type = fuel_type

    def show_info(self):
        return super().show_info()
        print(f"Fuel_Type: {self.fuel_type}")

class bike(vericle):
    def __init__(self, brand, wheels):
        super().__init__(brand, wheels)

    def show_info(self):
        return super().show_info()
    
def test_vehicles():
    Car = car("Toyota", 4, "Petrol")
    Bike = bike("Hero", 2) 

    Car.show_info()
    Bike.show_info()

        
if __name__ == "__main__":
    test_vehicles()
        