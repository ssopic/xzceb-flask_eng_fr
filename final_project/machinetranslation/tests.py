import unittest

from translator import english_to_french, french_to_english

class TestEnglishToFrench(unittest.TestCase):
    def test1(self):
        #test when hello should equal bonjour
        self.assertEqual(english_to_french("good night"),"bonne nuit") 
        #test when bye should equal Au revoir
        self.assertEqual(english_to_french("Goodbye"),"Au revoir")
        #test when "This is an english to french translator" should equal 
        # Ceci est un traducteur anglais vers français
        self.assertEqual(english_to_french("This is an english to french translator"),"C'est un traducteur anglais-français")

class TestFrenchToEnglish(unittest.TestCase):
    def test1(self):
        #test when Ceci est un traducteur anglais vers français should equal
        #This is an English to French translator
        self.assertEqual(french_to_english("Ceci est un traducteur anglais vers français"),"This is an English to French translator")
        #test when bonjour should equal hello
        self.assertEqual(french_to_english("Bonjour"),"Hello")
        #test when Au revoir should equall bye
        self.assertEqual(french_to_english("Au revoir"),"Goodbye")

unittest.main()