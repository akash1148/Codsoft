
# Task 1 Simple Calculator

print ("Welcome to Simple Calculator \n")

print("------------------")

def math():
    a= int(input("enter the 1st number:"))
    b= int(input("Enter the 2nd number:"))
    print("Enter the ArithmeticOperation you want to perform:")
    op= input("+\n-\n/\n*\n------------------\n")
    if(op=="+"):
        print("sum=",a+b)
    elif(op=="-"):
        print("subtract=",a-b)
    elif(op=="/"):
        print("division=",a/b)
    elif(op=="*"):
        print("multiply=",a*b)
    else:
        print("Invalid Operation Entered.")
    n=input("\nDo you want to reuse the Calculator??\nENter:\n1 for yes or -1 for no\n")
    if(n=="1"):
        math()
    elif(n=="-1"):
        exit()
math()    
