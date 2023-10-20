##################################################
#### **************************************** ####
#### !/usr/bin/python3                        ####
#### -*- coding: utf-8 -*-                    ####
#### @Time    : 2023/20/10 11:40              ####
#### @Author  : themanoftalent                ####
#### @Site:https://github.com/themanoftalent  ####
#### @Project : python-app                    ####
#### **************************************** ####
##################################################

tup2 = (1, 2, 3, 4, 5, 6, 7)
print(tup2)
print("tup2[1:4]: ", tup2[1:4])
print("-" * 70)

tup3 = ("a", "b", "c", "perro", "e", "f", "g", "i", "loro")
tup4 = tup2 + tup3
print(tup4)
print("-" * 70)

tup5 = tup4[0]
tup6 = tup4[1]
suma = tup5 + tup6
print(suma)
cantidad = len(tup3)
print(cantidad)
print(("-" + "^") * 40)
if "loro" and "gato" in tup3:
    print(tup3[2])
else:
    print(tup3[0])
print("-," * 30)
a = []
for x in tup2:
    L = x
    V = x * 2
    if x <= 5:
        a.append(x)
        print(a)
        print(V)

print("-+" * 30)

tup7 = ()
tup1 = ()
for i in range(1, 18, 5):
    tup7 += (i,)
    print(i)
print(i)
print(tup7)

print("-" * 70)

print(range(0, 16))

print("-.." * 30)

for i in range(2, 10, 2):
    tup1 += (i,)
print(tup1)

print("._" * 30)

lst = []
for i in range(0, 10, 2):
    lst.append(i)
print("lst: ", lst)
tup = tuple(lst)
print("tuple: ", tup)
print("_" * 30)

lsta = range(0, 10, 2)
tupla = tuple(range(1, 10, 2))
tuplaLC = [i for i in range(1, 11, 3)]
tuplaLCif = tuple(g ** 2 for g in range(0, 10, 2) if g <= 9)
listaLCif = [g ** 2 for g in range(0, 10, 2) if g <= 6]
rrr = tuple(i for i in range(1, 10, 2))
print(lsta)
print(tupla)
print(tuplaLC)
print(tuplaLCif)
print(listaLCif)
print(rrr)
