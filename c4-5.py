class publisher:
    def __init__(self,name):
        self.name=name

    def display(self):
        print("publisher name",self.name)


class book(publisher):
    def __init__(self,name,author,title):
        self.author=author
        self.title=title
        super().__init__(name)

    def display(self):
        super().display()
        print("name of author:",self.author)
        print("title of book:",self.title)




class python(book):
    def __init__(self,name,author,title,price,pages):
        self.price=price
        self.pages=pages
        super().__init__(name,author,title)

    def display(self):
        super().display()
        print("price:",self.price)
        print("pages:",self.pages)


name=input("enter name:")
author=input("name of author:")
title=input("enter title:")
price=int(input("price of book:"))
pages=int(input("no of pages:"))

obj=python(name,author,title,price,pages)
obj.display()

        
