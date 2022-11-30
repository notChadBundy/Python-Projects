# -*- coding: utf-8 -*-
"""
Created on Wed Jul 21 10:50:10 2021

@author: CHAD
"""


my_name=input('What is your name?')
print(f'Good day {my_name}')
my_surname=input('What is your Surname?')
print(f"Thank-you {my_name} {my_surname}")
feeling=input('Are you feeling Good today?(Y/N)')
if feeling=='y' or 'Y':
    print(f'Well Im glad, I hope you can spread some of your joy with me {my_name} <3')
else:
    print(f'Well Cheer-up, because you could have been dead today {my_name}')
    #Logical Error regarding if statement below
    
inn=input('Do you like Dungeons and dragons?(Y/N)')
if inn=='N' or 'n':
        print(f'Well {my_name}, neither do I! Thats for Nerds')
else:
        length=input(f'Thats so Cool! How Long have you been playing the game {my_name}?')
        print(f'Wow {my_name}, {length} is quite a long time!')
