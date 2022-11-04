d={}
n=int(input("enter size of dictionary"))
for i in range(0,n):
    keys=input("enter keys")
    values=input("enter values")
    d[keys]=values
print(d)
l=list(d.items())
l.sort()
print("ascending order is",l)
d=dict(l)
print("dictionary",d)
l.sort(reverse=True)
print("descending order is",l)
d=dict(l)
print("dictionary",d)
