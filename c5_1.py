f=open("sample.txt","r")
l=[]
for x in f:
	l.append(x.rstrip())
print(l)
f.close
