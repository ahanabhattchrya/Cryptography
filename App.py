'''
This is a simple personal project built with Python 3 by me (Ahana) to work on and enhance my skills in Python. This project was
started simply for practice purposes only. Additionaly to make sure I understood the code and logic behind this App I have commented
several lines with detailed description on what they do and how they work. 

This project was inspired by a python encryption/decryption project done in my linear algebra course, as well as a similar one done in 
my Systems programming course (CSE 220) in C.

General Outline/Goals of this project:
    - rearrange order of letters, do this by putting letters in even and odd positions
    - swap first two letters with the next two and so on
    - the user has to select an option between encrypt/decrypt so run an inifinte loop unless the user does so
    - in order to decrypt a message we have to convert the secret message into meaningful text/plaintext
'''

from tkinter import messagebox, simpledialog, Tk                #tkinter basically provides us with a GUI toolkit

#to see if tkinter is properly installed in your machine, type 'python -m tkinter' in the command line

'''
isEven() is a helper function that takes in a number and returns True if the number is even and false otherwise
'''
def isEven(number):
    return number % 2 == 0 

'''
The following functions getEvenLetters() and getOddLetters() take in a message and return the even and odd letters in a list format
from that message respectively.
'''
def getEvenLetters(message):
    evenLetters = []
    for letter in range(0, len(message)):
        if isEven(letter) == True:
            evenLetters.append(message[letter])
        else:
            letter += 1
    return evenLetters

def getOddLetters(message):
    oddLetters = []
    for letter in range(0, len(message)):
        if isEven(letter) == False:
            oddLetters.append(message[letter])
        else:
            letter += 1
    return oddLetters

