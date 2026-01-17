'''This is main.py'''
from internetAvailablity import internet_Available
from translator import *
from database import bin

def binary_search(bin , target):
    """
    sorted_dict : pre-sorted dictionary (by keys)
    target      : item name to search (string)
    returns     : value dict if found, else None
    """

    keys = list(bin.keys())  # already sorted once

    left = 0
    right = len(keys) - 1

    target = target.lower()

    while left <= right:
        mid = (left + right) // 2
        mid_key = keys[mid].lower()

        if mid_key == target:
            return bin[keys[mid]]

        elif mid_key < target:
            left = mid + 1
        else:
            right = mid - 1

    return None

if(internet_Available()):
    print("All Langauges Supported (Try Avoiding Hinglish)")
else:
    print('''Only english supported offline''')
    
text = input("\n\nEnter waste name only - ")
textTranslated= languageToEnglish(text)

result=binary_search(bin,textTranslated)
if result:
    print(
        f"✅ Item: {text}\n"
        f"   Category: {result['Item']}\n"
        f"   Bin: {result['Bin']}"
    )
else:
    print(f"❌ Item '{text}' not found in database")