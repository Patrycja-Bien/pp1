"""
18.	E-book is a digital book that can be read using a computer or other electronic devices 
(electronic book readers). Write a program in which define a class that describes states and 
behaviors of an  e-book. Each book has a title, author, number of pages and the current page number 
that is currently being read. It is possible to open a book - then we can read it. If a book is open,
it is possible to go to the next or previous page.
"""
class Ebook():
    def __init__(self,title,author,pages):
        self.title = title
        self.author = author
        self.pages = pages
        self.current_page = 1
        self.is_open = False
    def open(self):
        self.is_open = True
    def close(self):
        self.is_open = False
    def change_page(self):
        if self.is_open:
            self.current_page += 1
        else:
            print("The ebook is closed.")
    def status(self):
        print("Title: "+self.title+"\n"+"Author: "+self.author+"\n"+"Pages: "+str(self.pages)+"\n"+"Current page: "+str(self.current_page)+"\n")