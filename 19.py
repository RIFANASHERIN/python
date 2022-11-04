def swap(a,b):
    new_a=b[0]+a[1:]
    new_b=a[0]+b[1:]
    return new_a+' '+new_b
a=input("enter first string")
b=input("enter second string")

print(swap(a,b))
