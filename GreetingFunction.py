# -*- coding: utf-8 -*-
"""
Created on Tue Jun 28 23:38:04 2022

@author: CHAD
"""

# super Basic Function with arguments and parametres incorporated.
name = input("Hey whats your name fool?")
age = input("How old are you fool?")


# while age != float:
#    print('No Letters and Special Characters!!!')
#    break

def greet(name, age):
    print(f'Hello, How are you {name}?', f'I know that your {age} years old.')


def is_adult(age):
    if age >= 20:
        print("Greetings fellow adult :)")
    else:
        print("Sadly, your still a minor:)")


greet(name, age)
is_adult(age)
