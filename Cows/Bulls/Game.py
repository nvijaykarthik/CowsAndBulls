'''
Created on 20-May-2018

@author: nvijaykarthik
'''
import random

class Game(object):

    
    def __init__(self):
        '''
        Initializing the Game cows and bulls;
        '''
        print('''
The numerical version of the game is usually played with 4 digits, but can also be played with 3 or any other number of digits.

On a sheet of paper, the players each write a 4-digit secret number. The digits must be all different. 
Then, in turn, the players try to guess their opponent's number who gives the number of matches. 
If the matching digits are in their right positions, they are "bulls", if in different positions, they are "cows". Example:

Secret number: 4271
Opponent try: 1234
Answer: 1 bull and 2 cows (The bull is "2", the cows are "4" and "1")   
            ''')
        
        self.number=str(''.join(random.sample("0123456789", 4)))
        print("Number assigned is",self.number)
        self.cows=0
        self.bulls=0
    
    def play(self):
        playing=True
        sample=0
        while playing:
            self.cows=0
            self.bulls=0
            sample+=1
            print("Sample-",sample)
            userGuess=input("Try guessing the number (4 digit):")
            i=0
            for guess in userGuess:
                if self.number.__contains__(guess):
                    self.cows+=1
                if self.number[i]==guess:
                    self.bulls+=1
                if self.cows==4 and self.bulls==4:
                    print("Found the number")
                    playing=False
                    break
                i+=1
                
            print("Cows=",self.cows,"Bulls=",self.bulls)
            