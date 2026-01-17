'''This is a translator that can translate any text to English for the data base'''
'''deeptranslator for online translation

langdetect to detect lang offline

argostranslate to translate offline'''

'''Language Codes: langdetect returns standard ISO codes (like 'zh-cn' or 'en').

argostranslate generally uses standard codes too, but sometimes there are slight mismatches (e.g., Chinese might be 'zh' vs 'zh-CN').

Fix: If you get an error saying "Package not found," print the detected_lang code to see exactly what langdetect gave you.'''


from internetAvailablity import internet_Available

from deep_translator import GoogleTranslator
import argostranslate
from langdetect import detect

def translateGoogle(text):
    translated = GoogleTranslator(source='auto', target='en').translate(text) 
    return translated

def tranlateOffline(text):
    

    from_code = languageDetection(text)
    to_code = "en"
    translatedText = argostranslate.translate.translate(text, from_code, to_code)
    return translatedText
   

def languageDetection(text):
    return detect(text)

def languageToEnglish(text):
    if(internet_Available()):
        return translateGoogle(text)
    else:
        return tranlateOffline(text)
