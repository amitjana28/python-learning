# map, reduce and filter functions


# map(func,iterable) : It applies a given function to each element of an iterable

cube = lambda a: a*a*a

l = [2,5,6,8,9]

cubeList = map(cube,l)

cList = list(map(cube,l))

print(l)
print(list(cubeList))


# reduce(function,iterable) : It applies a given function cumulatively to an iterable, reducing to it a single value.
# Reduce function is a method of functools module so we need to import it before use

from functools import reduce
sum = reduce(lambda a,b:a+b, l)
print(sum)



# filter(function,iterable) : It is used to extract element form a iterable that satisfied the given condition
evenList = filter(lambda a: a%2==0,l)
print(list(evenList))

