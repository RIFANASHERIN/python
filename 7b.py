lst1=[]
print("enter first list")
n=int(input("enter number of elemnts:"))
for i in range(0,n):
    el=int(input("enter elements"))
    lst1.append(el)
print(lst1)

lst2=[]
print("enter second list")
n=int(input("enter number of elemnts:"))
for i in range(0,n):
    el=int(input("enter elements"))
    lst2.append(el)
print(lst2)
sum1=sum(lst1)
sum2=sum(lst2)

if(sum1==sum2):
    print("same sum")
else:
    print("not same sum")
