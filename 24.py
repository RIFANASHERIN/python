def fibonacci(n):
    a=0
    b=1
    if(n<0):
        print("incorrect")
    elif(n==0):
        print(a)
    elif(n==1):
        print(a, b)
    else:
        for i in range(1,n+1):
            print(a, end=" ")
            c=a+b
            a=b
            b=c
n=int(input("enter limit:"))
fibonacci(n)
