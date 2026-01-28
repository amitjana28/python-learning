class Animal:
    def __init__(self, name, type):
        self.name = name
        self.type = type

    def info(self):
        print("Animal name is {} and it is a {}".format(self.name, self.type))

class Dog(Animal):
    def action(self):
        print(self.name, " is walking")


class Horse(Animal):
    def action(self):
        print(f"{self.name} is running")




obj1 = Animal("tom", "cat")
obj2 = Dog("Bob","Dog")
obj3 = Horse("Badal","Horse")

obj1.info()
obj2.info()
obj3.info()


obj2.action()
obj3.action()


# There is a super() function is used to call  the parent class methods. it is commonly used in the child class’s __init__() method to initialize inherited attributes. 
# This way, the child class can leverage the functionality of the parent class.

class Bird(Animal):
    def __init__(self, name, type, bread):
        super().__init__(name, type)
        self.bread = bread

    def info(self):
        super().info()
        print("It is a {}".format(self.bread))

    def action(self):
        print(self.name, "is flying")


obj4 = Bird("Mitthu","Bird","Parrot")
obj4.info()
obj4.action()