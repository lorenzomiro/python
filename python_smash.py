#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jan 11 12:12:25 2019

@author: Miro
"""

#Show list of characters

print("SMASH PYTHON")

#Ask user(s) for number of players

users = int(input("How many players? "))

def get_player_count(users):

    while users > 9:
    
        print("WHOA TOO MANY USERS!!")
    
        users = int(input("How many players? "))
        
    while users < 1:
        
        print("WHOA NOT ENOUGH USERS!!")
    
        users = int(input("How many players? "))
        
get_player_count(users)
        
#Ask user for stage
        
def get_stage():
    
    stages = ['Lylat','Battlefield']
    
    print("Here are the stages: ", stages)
    
    stage = int(input("Which stage do you want to fight on? (The first stage is 1, the second stage is 2, etc.) "))
    
    print("Prepare to fight on", stages[stage-1] + "!")
    
get_stage()

def get_characters(users):
    
    characters = ['Mario','Kirby']
    
    for i in range(users):
        
        print("Here are the characters: ")
        
        character_number = 1
        
        for character_number in range(len(characters)):
            
            print(characters[character_number-1])
        
        players_character = input('Player ' + str(character_number) + ' select a fighter! ')
        
        if players_character == 'Mario':
            
            print('Mario!')
            
        if players_character == 'Kirby':
            
            print('Kirby')
            
        for players_character not in characters[i]:
            
            print("Who's that?")
            
            players_character = input('Player ' + str(character_number) + ' select a fighter! ')

        character_number += 1
        
        if character_number == users:
         
            continue
    
get_characters(users)

class controls:
    
    stocks = 3
    
    def controller():
        
        
        
        move = 'Enter a move, player '

#main() function is the game
'''        
def main():
    
  #  number_of_players = get_player_count()
    
   # stage_selection = get_stage()
    
main()
    
   
    players = get_player_count(users)
    
    for charact
    
main()
'''