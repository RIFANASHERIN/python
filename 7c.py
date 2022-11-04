l1=[]
l3=[]
print("first list elements:")
n=int(input("size of first list:"))
for i in range(0,n):
    el=int(input("enter elements:"))
    l1.append(el)
    print(l1)

l2=[]
print("second list elements:")
n=int(input("size of second list:"))
for i in range(0,n):
    el=int(input("enter elements:"))
    l2.append(el)
    print(l2)

def commonel(l1,l2):
  l3=[x for x in l1 if x in l2]
  return l3
print("duplicate elements are",commonel(l1,l2))
