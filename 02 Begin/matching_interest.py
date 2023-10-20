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


people = [
    {
        'name': "Mary",
        'interests': ['Football', 'Music', 'Dance', 'Books'],
        'gender': "female",
    },
    {
        'name': "Yulia",
        'interests': ['Football', 'Music', 'Dance', 'Books'],
        'gender': "female",
    },
    {
        'name': "Dapina",
        'interests': ['Music', 'Poker', 'Dance', 'Books'],
        'gender': "female",
    },
    {
        'name': "Ilıa",
        'interests': ['Poker', 'Theatre', 'Music', 'Books'],
        'gender': "female",
    },
    {
        'name': "Tanya",
        'interests': ['Football', 'Theatre', 'Dance', 'Basketball'],
        'gender': "female",
    },
    {
        'name': "Oksana",
        'interests': ['Dance', 'Poker', 'Football', ' Music'],
        'gender': "female",
    },
    {
        'name': "Inna",
        'interests': ['Books', 'Music', 'Football', 'Dance'],
        'gender': "female",
    },
    {
        'name': "Anna",
        'interests': ['Basketball', 'Theatre', 'Books', 'Music'],
        'gender': "male",
    },
    {
        'name': "Julia",
        'interests': ['Theatre', 'Football', 'Dance', 'Music'],
        'gender': "male",
    },
    {
        'name': "Angelika",
        'interests': ['Theatre', 'Football', 'Dance', 'Music'],
        'gender': "male",
    },
    {
        'name': "Emir",
        'interests': ['Theatre', 'Basketball', 'Poker', 'Music'],
        'gender': "male",
    },
    {
        'name': "Joker",
        'interests': ['Tennis', 'Music', 'Theatre', 'Basketball'],
        'gender': "male",
    },
    {
        'name': "Putin",
        'interests': ['Football', 'Poker', 'Basketball', 'Alcohol'],
        'gender': "male",
    },
    {
        'name': "Kagor",
        'interests': ['Football', 'Poker', 'Theatre', 'Music'],
        'gender': "male",
    },
]
matches = set()
for i in range(len(people)):
    for j in range(len(people)):
        if people[i]['gender'] == "female" and people[j]['gender'] == "male":
            if len(set(people[i]['interests']).intersection(set(people[j]['interests']))) > 0:
                if people[j]['name'] in matches:
                    break
                print(people[i]['name'] + " with " + people[j]['name'] + " have the following common interests: ")
                print(set(people[i]['interests']).intersection(set(people[j]['interests'])))
                matches.add(people[j]['name'])
                break
