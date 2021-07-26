import os

file = "abc.txt"
location ="C://Users//Pooja//Desktop//Python//C99//"
path = os.path.join(location, file)
os.remove(path)