class publisher:
	def __init__(self,title,author):
		self.title=title
		self.author=author
	def printf(self):
		print("book details = ",self.title,self.author)

class book(publisher):
	def __init__(self,price,pages):
		self.price=price
		self.pages=pages
		
	def printf(self):
		print("book details = ",pub.title,pub.author,self.price,self.pages)
		
pub=publisher("Introduction to python","james")	
b=book(2500,5000)
b.printf()	 
	
