# -*- coding: utf-8 -*-
"""
Created on Sun Aug  1 12:54:38 2021

@author: CHAD
"""

'''Rock, Paper, Scissors'''

import random
import os
import re

attempts_lists = []
objects_list['Rock', 'Paper', 'Scissors']
def show_score():
    if len(attempts_list) <= 0:
        print('there is currently no high score, its yours for the taking!!!')
    else:
        print(f'''the current high score is {} games''')
def start_game():
    random_object = str(random.choices(objects_list))
    print('Hello child! Welcome to the game of Rock, Paper, Scissors')
    player_name = input('What is your name?')
    lets_play = input(f'''Hi {player_name}, would you like to play a quick game of Rock, Paper, Scissors? (Enter Yes/No) ''')
    #Where the show_score fuction must be used
    attempts = 0
    show_score()
    while wanna_play.lower() == "yes":
        try:
            guess = input("pick")
            #not complete