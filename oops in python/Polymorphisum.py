# There are 2 types of polymorphism : runtime (Overriding) and compile time (Overloading)

# Overloading : 
class Calculator:
    def add(self, a=0, b=0, *args):
        result = a+b
        for num in args:
            result+=num
        return result
    

C1 = Calculator()

print(C1.add())
print(C1.add(4))
print(C1.add(4,5))
print(C1.add(45,14,10))
print(C1.add(42,18,56,85))




# Overriding : It is used in inheritanc We will learn this after learning Inheritance in python