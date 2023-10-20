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


class Animals:
    def vakvak(self):
        return self.strings['VakVakVak']

    def tuylu(self):
        return self.strings['Tuyum_var']

    def havhav(self):
        return self.strings['Vahvah']

    def kurk(self):
        return self.strings['Kürk']

    def meow(self):
        return self.strings['Meov']


class Ordek(Animals):
    strings = dict(
        vakvak="Vaaaaaak",
        tuylu="Ordegin beyaz tuyleri var",
        havhav="Ordek havlayamaz",
        kurk="Ordeğin kürkü yok",
        meow="Ordek miyavlayamaz"

    )


class insan(Animals):
    strings = dict(
        vakvak="İnsan ördek gibi vakvak yapar",
        tuylu="İnsan tüylü olabilir",
        havhav="İnsan köpek gibi havlayabilir",
        kurk="İnsanın kürkü yok",
        meow="İnsan kedi gibi miyavlayabilir."
    )


class Kopek(Animals):
    strings = dict(
        vakvak="KOpek ördek gibi vakvak yapamaz",
        tuylu="Kopek tüylü olabilir",
        havhav="köpek havlayabilir",
        kurk="Kopek kürkü var",
        meow="Kopek miyavlamaz."
    )

def kopekYazdir(Kopek):
    print(Kopek.havhav())
    print(Kopek.kurk())


def ordekYazdir(Ordek):
    print(Ordek.vakvak())
    print(Ordek.kurk())

def insanYazdir(insan):
    print(insan.havhav())
    print(insan.kurk())

def main():
    Donald=Ordek()
    Tumaz=Kopek()
    Ahmet=insan()

    print("kopekYazdir")
    for o in (Donald,Tumaz,Ahmet):
        kopekYazdir(o)




if __name__ == "__main__": main()
