# We can define function using def keyword

def sum(a,b):
    print(f"Sum of two numbers are {a+b}")
    return a+b

result = sum(2,5)
print(result)






# Types of argument in functions : Defaul, positional, keyword, Arbitary

# Default argument : here b is a default 0 value and work as a default argument,if someone does'nt pass b value it will default value
def compare(a,b=0):
    if(a>b): return a
    else: return b

print(compare(-4))
print(compare(4,8))
print(compare(0,3))






# Positional argument & Keyword argumanet
def printDetails(name,age):
    print(f"My name is {name} and I am {age} years old")

# here name and age are positional arguments so position should be same else it will give unexpected result
printDetails("Amit",25)
printDetails(23,"Rahul")

# here name and age are keyword arguments so position does'nt really matter just we need to mention the keyword of the parameter
printDetails(name="Ravi", age="45")
printDetails(age=62,name="Rohan")

# We can also pass positional only and keyword only arguments together using *, and /, symbol
def calculation(a,b,/,*,c,d):
    print(f"Sum of {a} and {b} is "+str(a+b))
    print(f"multiplication of {c} and {d} is "+str(c*d))

calculation(2,9,c=4,d=8)







# Arbitary argument : We can pass a variable number of argument to a function using special symbol *args(for non keywords arguments) and **kwargs(for keywords arguments)
# positional argument comes first then keyword argument
def arbitaryArgumentExample(*args,**kwargs):
    print("Below are non keyword arguments")
    for arg in args:
        print(arg)

    print("below are keyword arguments")
    for key, value in kwargs.items():
        print(f"{key} : {value}")


# Positional argument commes first then keyword
arbitaryArgumentExample("Amit Jana",25,isMarried=False,gender="Male")





# Anonymus or lambda function : function without the name using lambda keyword 
# syntex  function_name = lambda arguments_commma_seperated : return_expresion
cube = lambda a : a*a*a
print(cube(12))



# Passed by referanc and passed by value : Mutable objects beahaves like passed by referance, change inside the function affect original and Imutable behaves like passed by value, original remain unchanged
def fun(x):
    x[0]=20

def fun2(x):
    x=10

list = [40,80,120]
fun(list)
print(list)

a=5
fun2(a)
print(a)



# In python functions are treated as like numbers, string or any other variables. We can assign them to a variable, pass them as a argument into another function
# Return them from function, store them in datastructure like list, or dictionary


# Stored sum(a,b) function in f variable and used as f(a,b)
f = sum
print(f(45,65))
