'''
This is a simple personal project built with Python 3 by me (Ahana) to work on and enhance my skills in Python. This project was
started simply for practice purposes only. Additionaly to make sure I understood the code and logic behind this App I have commented
several lines with detailed description on what they do and how they work. 

This project was inspired by a python encryption/decryption project done in my linear algebra course.

General Outline/Goals of this project:
    - rearrange order of letters, do this by putting letters in even and odd positions
    - swap first two letters with the next two and so on
    - the user has to select an option between encrypt/decrypt so run an inifinte loop unless the user does so
    - in order to decrypt a message we have to convert the secret message into meaningful text/plaintext
'''

from tkinter import messagebox, simpledialog, Tk                #tkinter basically provides us with a GUI toolkit

#to see if tkinter is properly installed in your machine, type 'python -m tkinter' in the command line


