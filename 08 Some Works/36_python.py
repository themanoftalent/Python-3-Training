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

import requests
from bs4 import BeautifulSoup
import operator


def start(url):
    word_list = []
    source_code = requests.get(url).text
    soup = BeautifulSoup(source_code, 'html.parser')

    for post_text in soup.find_all('a', class_='index_singleListingTitles'):
        content = post_text.string
        words = content.lower().split()
        for each_word in words:
            word_list.append(each_word)

    clean_up_list(word_list)


def clean_up_list(word_list):
    clean_word_list = []

    symbols = "!@#$%^&*()_+{}:\"<>?,./;'[]-='"

    for word in word_list:
        for symbol in symbols:
            word = word.replace(symbol, "")

        if len(word) > 0:
            print(word)
            clean_word_list.append(word)


start('https://buckysroom.org/tops.php?type=text&period=this-month')
