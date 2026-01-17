'''This is main.py'''
from internetAvailablity import internet_Available
from translator import *

if(internet_Available()):
    print("All Langauges Supported (Try Avoiding Hinglish)")
else:
    print('''Only english supported offline''')
    
t = input("\n\nEnter waste name only - ")
t= languageToEnglish(t)
print(t)