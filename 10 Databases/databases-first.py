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

import sqlite3

def main():
    db = sqlite3.connect("test.db")
    db.row_factory = sqlite3.Row

    db.execute("drop table if exists test")
    db.execute("create table test (t1 text, i2 int)")
    db.execute("insert into test (t1, i2) values (?, ?)", ('one', 1))
    db.execute("insert into test (t1, i2) values (?, ?)", ('two', 2))
    db.execute("insert into test (t1, i2) values (?, ?)", ('three', 3))
    db.execute("insert into test (t1, i2) values (?, ?)", ('four', 4))
    db.commit()

    cursor = db.execute('select * from test order by i2')
    for row in cursor:
        #print(row)
        #print(dict(row))
        print(row['t1'], row['i2'])

if __name__ == "__main__": main()
