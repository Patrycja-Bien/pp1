movies = ["Up", "Drive", "Alien", "2012", "Knives Out"]

file = open("movies.txt","w")
for i in movies:
    file.write(i+"\n")
file.close()