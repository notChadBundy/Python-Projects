# -*- coding: utf-8 -*-
"""
Created on Tue Jun 28 22:35:01 2022

@author: CHAD
"""

#the syntax below represents a for loop.
def forloop1():
    names = ['Chad', 'Dexter', 'Lynn', 'James']
    for name in names:
        print(name)
#below is a for loop that fetches details from a dictionary      
def forloop2():
    #person is a dictionary
    person = {
        'name' : 'Chad',
        'age' : '20',
        'address' : 'Ennerdale'
        }
    print("P.S the output will be the same regardless of your choice!")
    choice = input(f"would you like the simple or complex Loop? Please use small caps")
    if choice == 'simple':
        for key in person:
            print(f"key:{key} value:{person[key]}")
    else:
    #this can be simplified by creating the loop as follows
        for key, value in person.items():
            print(f"key:{key} value:{value}")
        
forloop2()