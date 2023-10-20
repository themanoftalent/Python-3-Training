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


def trade_spider(max_pages):
  page = 1
  while page <= max_pages:
    url = 'https://buckysroom.org/trade/search.php?page=' + str(page)
    source_code = requests.get(url)
    plain_text = source_code.text
    soup = BeautifulSoup(plain_text, 'html.parser')

    # Here you can use Beautiful Soup to extract data from 'soup' variable
    # For example, you can find and print specific elements from the page

    # To find and print all the links on the page:
    for link in soup.find_all('a'):
      print(link.get('href'))

    # You can customize this code to extract the specific information you need.

    page += 1


# Specify the number of pages to scrape
max_pages = 5
trade_spider(max_pages)
