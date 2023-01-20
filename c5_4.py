import csv
with open("sample.csv",mode="r")as ob:
	d=next(ob)
	csvfile=csv.reader(ob)
	csvfile1=csv.reader(ob)
	n = int(input("enter column number:"))
	try:	
		for x in csvfile:
			print(x[n-1])
	except IndexError:
		print(" invalid coloumn count ")
