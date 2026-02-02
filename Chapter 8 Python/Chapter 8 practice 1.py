a = int(input("enter the number:"))
b = int(input("enter the number:"))
c = int(input("enter the number:"))

def fun1():
    if(a>b and a>c):
        print("a is the greatest number")

    elif(b>c and b>a):
        print("b is the greatest number")

    else:
        print("c is the greatest number")

fun1()        