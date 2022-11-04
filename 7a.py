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
l1=len(lst1)
l2=len(lst2)
if(l1==l2):
    print("these two lists have same length")
else:
    print("not same length")
