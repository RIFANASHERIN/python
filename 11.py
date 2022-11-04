
l1=input("enter names").split()
print(l1)
d={}
for name in l1:
   d[name]=0
   for c in name:
        if(c=='a'):
            d[name]=d[name]+1
print("count(a):",d) 
