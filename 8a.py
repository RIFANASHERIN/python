l=[]
p=[]
n=int(input("how many numbers you want to enter:"))
for i in range(0,n):
    el=int(input("enter elements:"))
    l.append(el)
    print(l)
print("positive numbers are:")
for i in range(0,n):
   if(l[i]>=0):
        p.append(l[i])
print(p)

