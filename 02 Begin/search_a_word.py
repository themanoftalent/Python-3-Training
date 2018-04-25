'''1
^

Matches beginning of line.

2
$

Matches end of line.

3
.

Matches any single character except newline. Using m option allows it to match newline as well.

4
[...]

Matches any single character in brackets.

5
[^...]

Matches any single character not in brackets

6
re*

Matches 0 or more occurrences of preceding expression.

7
re+

Matches 1 or more occurrence of preceding expression.

8
re?

Matches 0 or 1 occurrence of preceding expression.

9
re{ n}

Matches exactly n number of occurrences of preceding expression.

10
re{ n,}

Matches n or more occurrences of preceding expression.

11
re{ n, m}

Matches at least n and at most m occurrences of preceding expression.

12
a| b

Matches either a or b.

13
(re)

Groups regular expressions and remembers matched text.

14
(?imx)

Temporarily toggles on i, m, or x options within a regular expression. If in parentheses, only that area is affected.

15
(?-imx)

Temporarily toggles off i, m, or x options within a regular expression. If in parentheses, only that area is affected.

16
(?: re)

Groups regular expressions without remembering matched text.

17
(?imx: re)

Temporarily toggles on i, m, or x options within parentheses.

18
(?-imx: re)

Temporarily toggles off i, m, or x options within parentheses.

19
(?#...)

Comment.

20
(?= re)

Specifies position using a pattern. Doesn't have a range.

21
(?! re)

Specifies position using pattern negation. Doesn't have a range.

22
(?> re)

Matches independent pattern without backtracking.

23
\w

Matches word characters.

24
\W

Matches nonword characters.

25
\s

Matches whitespace. Equivalent to [\t\n\r\f].

26
\S

Matches nonwhitespace.

27
\d

Matches digits. Equivalent to [0-9].

28
\D

Matches nondigits.

29
\A

Matches beginning of string.

30
\Z

Matches end of string. If a newline exists, it matches just before newline.

31
\z

Matches end of string.

32
\G

Matches point where last match finished.

33
\b

Matches word boundaries when outside brackets. Matches backspace (0x08) when inside brackets.

34
\B

Matches nonword boundaries.

35
\n, \t, etc.

Matches newlines, carriage returns, tabs, etc.

36
\1...\9

Matches nth grouped subexpression.

37
\10

Matches nth grouped subexpression if it matched already. Otherwise refers to the octal representation of a character code.'''
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
