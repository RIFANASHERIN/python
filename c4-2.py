class bank:
    def __init__(self,ac_no,ac_name,ac_type,balance):
        self.ac_no=ac_no
        self.ac_name=ac_name
        self.ac_type=ac_type
        self.balance=balance
        

    def deposit(self):
        amt=int(input("enter amount to deposit:"))
        self.balance=self.balance+amt
        return (self.balance)
    def withdraw(self):
        amt=int(input("enter amount to withdarw:"))
        if amt>self.balance:
            print("balance is not sufficient")
        else:
            self.balance=self.balance-amt
            return self.balance

    def checkbalance(self):
        print("balace is",self.balance)

ac_no=int(input("enter ac number:"))
ac_name=input("enter name of account holder:")
ac_type=input("account type:")
balance=0
b=bank(ac_no,ac_name,ac_type,balance)
print("\n 1.deposit \n 2.withdraw \n 2.check balance \n")
while(True):
    c=int(input("enter choice:"))
    if c==1:
        b.deposit()

    elif c==2:
        b.withdraw()

    elif c==3:
        b.checkbalance()
    else:
        break
