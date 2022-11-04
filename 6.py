print("list of leap years between given two years")
start=int(input("enter starting year:"))
end=int(input("enter ending year:"))
for year in range(start,end):
    if((year%4==0) and (year%100!=0)) or (year%400==0):
        print(year)
