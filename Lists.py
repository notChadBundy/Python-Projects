# -*- coding: utf-8 -*-
"""
Created on Sun Aug  1 17:02:01 2021

@author: CHAD
"""

#This is a Number List

numbers = [1, 2, 3, 4]
letters = ['A', 'B', 'C', 'D']
your_name = input('''Hello what is your Name?''')
c2 = input(f'''So {your_name},Which list would you like to interact with? (Enter: [L]etters or [N]umbers)''')
c1 = input(f'''Okay, {your_name}, would you like to view or edit a List? (Enter: [v]iew or [e]dit) ''')
def VieworEdit(numbers, letters, c1, c2):
    if c1.lower() == 'v' or 'view':
        print(numbers)
        print('Thank You Have a Good Day')
    elif c1.lower() == 'e' or 'edit':
        add_number = input('Please input your new number')
        numbers.append(add_number)
        print(numbers)
        print('Thank You Have a Bad Day')
    
#def WhichList(numbers, letters, your_name, c2):
   # your_choice = input('Numbers or Letters? (Enter: L/N)')
    #if your_choice.lower() == 'l':
    #    print(letters)
    #elif your_choice.lower() == 'n':
    #    print(numbers)
    #elif your_choice.lower() != 'l' or 'n':
   #     print('Who are you trying to fool???')
        
