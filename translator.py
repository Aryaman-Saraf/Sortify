'''This is a translator that can translate any text to English for the data base'''
'''deeptranslator for online translation'''

from internetAvailablity import internet_Available

from deep_translator import GoogleTranslator


def translateGoogle(text):
    translated = GoogleTranslator(source='auto', target='en').translate(text) 
    return translated

def languageToEnglish(text):
    if(internet_Available()):
        return translateGoogle(text)
    else:
        return text
