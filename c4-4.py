class time:
    def __init__(self,hour,minute,second):
        self._hour=hour
        self._minute=minute
        self._second=second

    def __add__(self,other):
        seconds=(self._second+other._second)%60
        minutes=(self._minute+other._minute)%60 + (self._second+other._second)//60
        hours=(self._hour+other._hour) +  (self._minute+other._minute)//60 
        print(hours,":",minutes,":",seconds)

h1=int(input("enter hpur:"))
m1=int(input("enter minute:"))
s1=int(input("enter second:"))
h2=int(input("enter hpur:"))
m2=int(input("enter minute:"))
s2=int(input("enter second:"))

t1=time(h1,m1,s1)
t2=time(h2,m2,s2)

t1+t2



