# -*- coding: utf-8 -*-
"""
Created on Thu May 31 09:01:29 2018

@author: Kenneth Amoah Nyame
"""

# Newton- Raphson
epsilon = 0.01
y = 810.0
guess = y / 2.0
numGuesses = 0
while abs(guess*guess - y) >= epsilon :
    numGuesses += 1
    guess = guess - (((guess ** 2)-y) / (2 *guess))
print('numGuesses = ' + str(numGuesses)) 
print('Square root of ' + str(y) + ' is about ' + str(guess))   