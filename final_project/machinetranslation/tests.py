import unittest
from translator import french_to_english 
from translator import english_to_french

class testMyModuleF(unittest.TestCase):
    def test_french_to_english(self):
        self.assertEqual(french_to_english('Bonjour'),('Hello'))
        self.assertNotEqual(french_to_english('Bonjour'),('Bonjour'))
    def test_french_to_english2(self):
        self.assertTrue(french_to_english('None'), (''))

class testMyModuleE(unittest.TestCase):
    def test_english_to_french(self):
        self.assertEqual(english_to_french('Hello'),('Bonjour'))
        self.assertNotEqual(english_to_french('Hello'),('Hello'))
    def test_english_to_french2(self):
        self.assertTrue(english_to_french('None'), (''))
unittest.main()