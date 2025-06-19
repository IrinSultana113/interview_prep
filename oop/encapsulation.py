#Encapsulation is used to store data privated or protected. It was not to get access to the data. To access the data, we can use some method like the getter method, the setter method.
class employee:
    def __init__(self, name, id):
        self.name = name  # public variable
        self.__id = id  # private variable. Double underscore means we can make the variable private
                        # Single underscore means we can make the variable potected


    def get_id(self):# getter method. A getter method is used to read a private variable
        return self.__id  
    
    def set_id(self, id):  # setter method. A setter method is used to update a private variable with validation.
        if 0 <= id <= 100:
            self.__id = id

        else: 
            print("Invalid grade")


employee = employee("Irin", 4) 
print("Name:", employee.name) 
print("Initial Grade:", employee.get_id())
employee.set_id(6)   
print("Updated Grade:", employee.get_id())   


 

