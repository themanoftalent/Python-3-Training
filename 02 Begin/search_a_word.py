import re

a_text = "We are the protector of :the universe!"

matchme = re.search('\w{9}', a_text)
matchme2 = re.search(r'u\w{7}', a_text) #istediğin harfle başlamak için önüne o harften koy
matchme3 = re.search(r'^\w{2}', a_text)

if matchme:
    print("Found ", matchme.group())
else:
    print("Nothing found")
if matchme2:
    print("Found ", matchme2.group())
else:
    print("Nothing found")

if matchme3:
    print("Found ", matchme3.group())
else:
    print("Nothing found")
print("-----------------------------------")

twoText = """macfeet 
akifium
careermacfeet	
"""
yazdir1 = re.findall(r"^\w", twoText)
yazdir1 = re.findall(r"^\w", twoText, re.MULTILINE)
print(yazdir1)
print(yazdir1)
print("-----------------------------------")

line = "Cats are smarter than dogs"

matchObj = re.match(r'(.*) are (.*?) .*', line, re.M | re.I)

if matchObj:
    print("matchObj.group() : ", matchObj.group())
    print("matchObj.group(1) : ", matchObj.group(1))
    print("matchObj.group(2) : ", matchObj.group(2))
else:
    print("No match!!")
