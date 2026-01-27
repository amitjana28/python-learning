# There are 2 types of loop in pyhton : for and while

list = ["Apple","Banana","Cherry","Dragerfruit"]
for i in range(2,21,2):
    print(i,end=", ")
print()

for x in list:
    print(x,end=' | ')


student = {1:"Amit",2:"Rahul",3:"Arnab",4:"Debu"}
print()
print("List of Students : ")
for keys,value in student.items():
    print(f"{keys} : {value}")

for keys in student:
    print(keys)

for values in student.values():
    print(values)





# While loops :
n = 20
while n>1:
    print(n,end=", ")
    n-=2



# Loop control statement are like break: when we want to come out from the loop when condition met
# continue: when we want toignore that condition
# pass : it is used in classes, functions, loops when we want the existance of the block but don't want to do anything
n=0
while n<20:
    print(n, end=" | ")
    n+=1
    if n==15:
        break