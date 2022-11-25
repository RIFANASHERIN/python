def longest(words):
	heighest=0
	longest=""
	for wrd in words:
		count=0
		for a in wrd:
			count=count+1
		if(heighest<count):
			heighest=count
			longest=wrd
	print("longest word:",longest)
	print("number of characters:",heighest)

words=input("enter words:").split()
longest(words)
	
