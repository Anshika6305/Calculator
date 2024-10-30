import math as m
print("If you want to perform arithematic operation enter a")
d=input("what do you want to perform:")
if d=="a":
    a=float(input("Enter any number: "))
    b=float(input("Enter another number: "))
    print("To find remainder type % and to find quotint type //")
    c=input("Enter the operaational sign: ")
    if(c=="+"):
        print("Addition of given number is: ",a+b)
    elif(c=="-"):
        print("subtraction of given number is: ",a-b)
    elif(c=="*"):
        print("Multiplication of given number is: ",a*b)
    elif(c=="/"):
        print("Division of given number is: ",a/b)
    elif(c=="rem"):
        print("remainder of given number is: ",a%b)
    elif(c=="//"):
        print("floor div of given number is: ",a//b)
    else:
        print("Try Something Else!")
elif d=="power":
    num=float(input("enter any number:"))
    power=float(input("enter any number:"))
    res=num**power
    print(res)
elif d=="root":
    a=float(input("Enter any number: "))
    c=m.sqrt(a)
    print("square root of given number is: ",c)
elif d=="log":
    base=int(input("Enter base:"))
    a=int(input("Enter number:"))
    b=m.log(a,base)
    print(b)

else:
    print("OOPS! Somthing Went Wrong.........")
