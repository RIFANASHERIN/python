print("two dictionaries")
dict1={}
n=int(input("enter number of items"))
for i in range(0,n):
    key=input("enter the key")
    value=input("enter the value")
    dict1[key]=value
print(dict1)

dict2={}
n=int(input("enter number of items"))
for i in range(0,n):
    key=input("enter the key")
    value=input("enter the value")
    dict2[key]=value
print(dict2)

print("merging")
print("-------------------------------------------------------------------------------")
d3={**dict1, **dict2}

for k,v in d3.items():
    if k in dict1 and k in dict2:
        d3[k]=[v,dict1[k]]
print(d3)
