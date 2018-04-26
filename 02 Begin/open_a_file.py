'''mytext.txt:
01 a new beginning
02 developing
03 improving
04 finalizing
05 fin
'''

with open("Mytext.txt","r") as f:
    for line in f.read():
        print(line, end="")
