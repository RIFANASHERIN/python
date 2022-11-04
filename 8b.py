l=[]
p=[]
n=int(input("how many numbers you want to enter:"))
for i in range(0,n):
    el=int(input("enter elements:"))
    l.append(el)
    print(l)
print("squares of numbers are")
n=[]
n=[x*x for x in l if x>0]
print(n)
