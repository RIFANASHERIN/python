l1=[]
n=input("enter numbers").split()
for i in n:
    if int(i)>100:
        l1.append("over")
    else:
        l1.append(i)
print(l1)
