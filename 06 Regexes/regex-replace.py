
import re

def main():
    fh = open('raven.txt')
    for line in fh:
        print(re.sub('(Len|Neverm)ore', '###', line), end = "")

if __name__ == "__main__": main()
