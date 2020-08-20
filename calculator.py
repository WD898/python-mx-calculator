# calculator

print("--------Welcome to MX Calculator--------")
print("-----Developed by (Swarup Bhagwat.)-----")
print("-----------------V1.3-------------------")

# fuctions


def add(num1, num2):
    addition = num1 + num2
    print("Your answer is : " ,num1, "+",num2,"=", addition)
    return addition



def sub(num1,num2):
     substraction = num1 - num2
     print("Your answer is : " ,num1, "-",num2,"=", substraction)
     return substraction


def multi(num1, num2):
    multiplaction = num1 * num2
    print("Your answer is : " ,num1, "*",num2,"=",multiplaction)
    return multiplaction

def div(num1,num2):
    devision =num1 /num2
    print("Your answer is : " ,num1, "/",num2,"=",devision)
    return devision


# if else statment

opr = input("Please select the operator :\n + - * / ")
if opr == "+":

     add(int(input("First number : ")), int(input("Second number : ")))

elif opr == "-":
    sub(int(input("First number : ")), int(input("Second number : ")))

elif opr =="*":
    multi(int(input("First number : ")), int(input("Second number : ")))

elif opr =="/":
    div(int(input("First number : ")),int(input("Second number : ")))
















