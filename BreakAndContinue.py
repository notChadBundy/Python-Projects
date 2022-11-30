# -*- coding: utf-8 -*-
"""
Created on Tue Jun 28 23:22:41 2022

@author: CHAD
"""


number = 0

def breakandcontinue1():
    while number <= 10:
        if number == 5:
            break
        
def breakandcontinue2():
        while number < 10:
            number += 1
            if number < 5:
                continue
            elif number == 11:
                break
        else: print(f'complete')
        print(number)
    #number += 1