name = input("Enter your full name here: ")
initials = name[0: 1] + '. ' + name[name.find(' ') + 1: name.find(' ') + 2] + '. '
name2 = name[name.find(' ') + 1:]
if name2.find(' ') > 0:
    initials += name2[name2.find(' ') + 1: name2.find(' ') + 2] + '. '
    print(initials)
else:
    print(initials)
