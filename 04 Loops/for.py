def main():

    # For loop can use any iterator.
    # be it file input, containers, strings
    fb = open('lines.txt')
    for line in fb.readlines():
        print(line, end = "")

    for each_number in (1,2,3,4,5):
        print(each_number)

    for each_number in [1,2,3,4,5]:
        print(each_number)

    for each_character in 'string':
        print(each_character)


    # How about index?
    for i, a_char in enumerate('this is a string'):
        if a_char == 's':
            print("Index {} is an s ".format(i))


if __name__ == "__main__": main()
