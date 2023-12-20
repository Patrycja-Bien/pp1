"""
10.	Create a class that represents pieces of music. Define a class constructor that allows you to 
set the initial values of the music piece (artist, track title, album, year) when the object is 
created. Complete the class with the __str__ method returning the song data as a string, in the 
format as below (4 lines). Then, create two objects that represent two different pieces of music. 
Display these objects. 
"""

class Music():
    def __init__(self,author,song,album,year):
        self.author = author
        self.song = song
        self.album = album
        self.year = year
    def __str__(self):
        return  "Performer: "+self.author+"\n"+"Song: "+self.song+"\n"+"Album: "+self.album+"\n"+"Year: "+str(self.year)
one = Music("Author1","Song1","Album1",2001)
two = Music("Author2","Song2","Album2",2002)

print(one)
print(two)