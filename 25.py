def total(l1):
	tot=0
	for i in l1:
		tot=tot+i
	print("total sum:", tot)
		

l1=[]
n=int(input("enter size"))
for i in range(0,n):
	el=int(input("enter elements"))
	l1.append(el)
print(l1)
total(l1)	
