def sum(a,b):
    c=a+b
    print("The sum of two number=",c)

def sub(a,b):
    c=a-b
    print("The subtraction of two number=",c)

def mul(a,b):
    c=a*b
    print("The multiplication of two number=",c)

def div(a,b):
    c=a/b
    print("The division of two number=",c)

while True:
    print("choose operation:+,-,*,/ or enter 0 for exit")  
    operation=input("enter the operation:")  
    
    if operation =='+':
        num1= int(input("enter first number:"))
        num2= int(input("enter second number:"))
        sum(num1,num2)
    elif operation =='-':
        num1= int(input("enter first number:"))
        num2= int(input("enter second number:"))
        sub(num1,num2)
    elif operation =='*':
        num1= int(input("enter first number:"))
        num2= int(input("enter second number:"))
        mul(num1,num2)
    elif operation =='/':
        num1= int(input("enter first number:"))
        num2= int(input("enter second number:"))
        div(num1,num2)
    elif operation == "0":
        break 
    else:
        print("invalid operation..write again")
 