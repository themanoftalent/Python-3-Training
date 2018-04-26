def main():
    infile = open('bigfile.txt', 'r')
    outfile = open('bigfile_copy.txt', 'w')
    buffersize = 50000 # bytes
    buffer = infile.read(buffersize)
    while len(buffer):
        outfile.write(buffer)
        buffer = infile.read(buffersize)


if __name__ == "__main__": main()
