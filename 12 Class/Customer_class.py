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

from random import randint
global stocks
class Customer(object):
    def __init__(self, name, balance = 0.0):
        self.name = name
        self.balance = balance
        self.stock = Stock(0)

    def __init__(self, name,stocks, balance = 0.0):
        self.name = name
        self.balance = balance
        self.stock = Stock(stocks)

    def getTotalValue(self):
        return(self.balance + self.stock.totalValue())

    def getBalance (self):
        return self.balance

    def getName (self):
        return self.name

    def withdrawl (self, value = 0.0):
        if(self.balance >= value):
            self.balance -= value
        else:
            raise RuntimeError('Insufficient Funds')

    def deposit (self, value = 0.0):
        self.balance += value

    def buyStock (self, numShares):
        if (Stock.getCurrentStockPrice() * numShares <= self.balance):
            self.balance -= Stock.getCurrentStockPrice() * numShares
            self.stock.buy(numShares)
        else:
            raise RuntimeError('Insufficient Funds')

    def sellStock(self, numShares):
        if(self.stock.getNumberOfShares() >= numShares):
            self.deposit(self.stock.sell(numShares))
        else:
            raise RuntimeError('Insufficient Number of Shares')



class Stock(object):

    currentStockPrice = 125.25

    def __init__(self, shares):
        self.shares = shares

    @staticmethod
    def getCurrentStockPrice():
        return Stock.currentStockPrice

    @staticmethod
    def newDay():
        Stock.setCurrentStockPrice()

    @staticmethod
    def setCurrentStockPrice():
        Stock.currentStockPrice = randint(0, 20000) / 100

    def getNumberOfShares(self):
        return self.shares

    def buy(self, shares):
        self.shares += shares
        Stock.setCurrentStockPrice()

    def sell(self, shares):
        value = 0.0
        if (self.shares >= shares):
            self.shares -= shares
            value = shares * Stock.getCurrentStockPrice()
        else:
            raise RuntimeError('Insufficient Stocks')
        Stock.setCurrentStockPrice()
        return value

    def totalValue(self):
        return Stock.getCurrentStockPrice() * self.getNumberOfShares
