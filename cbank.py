class bank:
	def __init__(self,an,na,at,b):
		self.acno=an
		self.name=na
		self.acty=at
		self.bal=b
	def printf(self):
		print("account no: %d name: %s account type: %s balance= %d " %(self.acno,self.name,self.acty,self.bal))
	def deposit(self):
		self.printf()
		self.bal=self.bal+int(input("enter the deposit amount: "))
		self.printf()
	def withdraw(self):
		self.printf()
		self.bal=self.bal-int(input("enter the withdraw amount: "))
		self.printf()

n1,n2= [int(x) for x in input("enter the account no  and bal :").split() ]
n3,n4=input("enter the name and account type ").split()
ba=bank(an=n1,na=n3,at=n4,b=n2)
choice=int(input("press 1 for deposit \n 2 for withdraw \n"))
if choice == 1:
  
	ba.deposit()

elif choice == 2:

	ba.withdraw()
else:
	print("invalid choice")













