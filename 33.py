def string(n):
	length=len(n)
	if(length>2):
		if(n[-3:]=='ing'):
			n=n+'ly'
		else:
			n=n+'ing'
	print(n)
n=input("enter string:")
string(n)
