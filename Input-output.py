# Input/output Leacture

# Input : In python we use input() function for taking user input
age = input("Enter yur age : ")
name, country = input("Enter your name and country :").split(",")
print(f"Hello {name}! Welcome to {country}. You are {age} years old.")
print("Hello {}! Welcome to {}. You are {} years old.".format(name,country,age))
print("Hello " +name+"! Welcome to"+ country+". You are "+age+" years old.")

# Input() function always take values as String we need to convert them in required data type using type conversion functions like int(), floot(), str()
print(type(age))
age = int(age)
print(type(age))
age = str(age)
print(type(age))



# Output : In python there is print(value, sep, end, file, flush) function for print any values on screen

print("Hello my name is Amit.")
print("My","name","is","Amit","Jana", sep="_")

print("Hello!",end=" ")
print("My name is amit jana")

fruits = ["Apple","Graps","Orange","papaya"]
print(fruits)

for x in fruits:
    print(x,end=" | ")

