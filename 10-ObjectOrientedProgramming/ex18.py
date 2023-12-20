"""
Place the class describing e-books in a separate file/module. In the main program file, try 
using the e-book:
a.	Create a book with a title, author, number of pages (check how to set the initial values of the 
fields at the time of creating the object using the __init__ method / constructor and passing the 
initial values as arguments to the method call)
b.	Open a book
c.	Display a book status (title, author, page numbers, current page no)
d.	Read a few pages
e.	Display a book status
f.	Close a book
g.	Read a few pages (it should not be possible to perform this operation - display the message that 
the book is closed).

"""
from mod18 import Ebook

book = Ebook("The body","Stephen King",192)
book.open()
book.status()
book.change_page()
book.change_page()
book.change_page()
book.change_page()
book.status()
book.close()
book.change_page()