# define class

class Car:
    # Define attribute or class variables
    type = "EV"

    # Define constructor
    def __init__(self,name,color):
        # Attributes or instance variables
        self.name = name
        self.color = color
        print("New Object is created")

    # Define destroctor
    def __del__(self):
        print("Object is destroyed")

    # Methods
    def printDetails(self):
        print(f"You have {self.color} {self.name} of type {self.type}.")


# Object created
Honda = Car("Honda","Red")

# Method called
Honda.printDetails()

# Changed class and instance variables
Honda.type = "Petrol"
Honda.name = "BMW"
Honda.color = "Blue"

# Method called
Honda.printDetails()

# Object Destroyed
del Honda

# Method call after object destroyed give error
# Honda.printDetails()