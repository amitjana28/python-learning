# There are few conditional statements in python like if, if-else, if-elif-else, match case, ternary

# if-else
print("Choose option for your gender :\n1.Male\n2.Female")
gender = int(input("Please provide input either 1 or 2 in digits : "))

if gender==1:
    print("You are a male")
else:
    print("you are a female")



# if-elif-else 
age = int(input("Enter the age :"))

if age<0:
    print("Incorrect age! Please provide valid age")
elif age>=18:
    print("Eligible for vote")
else:
    print("Unable to vote")


# ternary
number = int(input("Enter a number : "))
isEven = True if number%2==0 else False
print("Giver number {} is a even : {}".format(number,isEven))


# Match case
Grade = input("Please provide your grade A, B, C, D, E:")

match Grade:
    case 'A'|'a':
        print("Very Good! Keep doing the same")
    case 'B'|'b':
        print("Good! Keep it up")
    case 'C'|'c':
        print("Average! Need improvement")
    case 'D'|'d':
        print("Poor! Performance! Please improve")
    case 'E'|'e':
        print("Very Poor! Need counceling for improvement")
    case _:
        print("Incorrect Grade! Please provide Grade from A,B,C,D and E")