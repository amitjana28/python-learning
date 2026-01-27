"""
Docstring for Python_Program.basics
Below are few ways for addtion like using function, lambda function, sum(list) function, operator.add()
"""

def addition(a,b):
    return a+b

a,b = input("Enter first number and second number comma seperated : ").split(",")

print(addition(int(a),int(b)))




add = lambda a,b: a+b
print(add(154,253))



list = [12,56,95,12,53]
print(sum(list))


import operator
print(operator.add(154,565.25))