l1=[]
line=input("enter sentence")
word=input("enter the word that you want to count")
count=0
l1=line.split()
for wrd in l1:
    if(word==wrd):
        count=count+1
print("count of the word is:")
print(count)
