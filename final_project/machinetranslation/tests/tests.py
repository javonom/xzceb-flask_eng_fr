import unittest
from translator import english_to_french
from translator import french_to_english

class TestTranslator(unittest.TestCase):
    def test_e2f1(self):
        self.assertEqual(english_to_french('Hello, how are you today?'),'Bonjour, comment vous êtes aujourd\'hui?')
    def test_e2f_hello(self):
        self.assertEqual(english_to_french('Hello'),'Bonjour') 
    def test_e2f_hello2(self):
        self.assertNotEqual(english_to_french('None'),'') 
    def test_e2f_hello3(self):
        self.assertNotEqual(english_to_french(0),0)


class TestTranslator1(unittest.TestCase):
    def test_f2e1(self):
        self.assertEqual(french_to_english('Bonjour, comment vous êtes aujourd\'hui?'),'Hello, how are you today?')
    def test_f2e_bonjour(self):
        self.assertEqual(french_to_english('Bonjour'),'Hello') 
    def test_f2e_bonjour2(self):
        self.assertNotEqual(french_to_english('Néant'),'') 
    def test_f2e_bonjour3(self):
        self.assertNotEqual(french_to_english(0),0)
unittest.main()