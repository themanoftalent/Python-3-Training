def main():
    infile = open('olives.jpg', 'rb')
    outfile = open('olives-copy.jpg', 'wb')
    buffersize = 50000
    buffer = infile.read(buffersize)
    while len(buffer):
        outfile.write(buffer)
        buffer = infile.read(buffersize)
        print(".")
    print("Done")
if __name__ == "__main__": main()
