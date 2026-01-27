# Class is a blueprint of an object, it defines set of attributes and methods.
# Class is created by class keyword, attributes are variable belongs to class, attributes are always public and can be accessed using dot operator
# __init__ method is a constructor in python automatically call when a new method is created
# Self parameter is a reference of a current instance of a class

# In below example name and age are class attribute
class Student:
    school = "B.N.Public School" #This is a class variable
    def __init__(self,name,age):
        self.name = name #This is a instance variable
        self.age = age  #This is a instance variable

    def printDetails(self):
        print(f"Name of student is {self.name} and age is {self.age}\nMy school name is {self.school}")



S1 = Student("Ravi",45)
S2 = Student("Amit",25)
S1.printDetails()
S2.printDetails()


print(S1.school,S2.school)

Student.school = "DAV"

print(S1.school,S2.school)

S1.printDetails()