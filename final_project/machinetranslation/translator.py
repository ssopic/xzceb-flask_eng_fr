"""translator.py
Translates from English to French and vice-versa
"""
from deep_translator import MyMemoryTranslator

def english_to_french(english_text):
    """Trasnaltes English to French
    The arguments are the text itself(one string only)
    The ouput is the string in another language """
    french_text=MyMemoryTranslator(source="en", target="french").translate(english_text)
    return french_text

def french_to_english(french_text):
    """Translates French to English
    The arguments are the text itself(one string only)
    The ouput is the string in another language """
    english_text=MyMemoryTranslator(source="fr", target="english").translate(french_text)
    return english_text
    