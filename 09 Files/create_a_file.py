# create and open a file

with open("NewFile.txt", "a+") as f:
    f.write("We are writing some new text here.")
    f.close()

f = open("NewFile.txt", "r+")
radme = f.read(33)
print(radme)
f.close()
