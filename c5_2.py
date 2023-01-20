f=open("sample.txt","r")
l=[]
j=1
for x in f:
	if(j%2 !=0):
		l.append(x.rstrip())
	j=j+1
print(l)
f.close
f2=open("sample2.txt","w")

for c in range(len(l)):
	f2.write(l[c]+"\n")

f2.close()
	

