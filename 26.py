def factorial(n):
	f=1
	for i in range(1,n+1):
		f=f*i
	print("factorial:",f)
n=int(input("enter a number"))
factorial(n)
