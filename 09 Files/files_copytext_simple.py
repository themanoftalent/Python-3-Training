
def main():
    infile = open('lines.txt', 'r')
    outfile = open('output.txt', 'w')
    for line in infile:
        print(line, file = outfile, end = '')

if __name__ == "__main__": main()
