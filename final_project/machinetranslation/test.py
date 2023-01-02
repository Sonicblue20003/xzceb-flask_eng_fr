import unittest
from translator import frenchToEnglish, englishToFrench

class testMyModuleF(unittest.TestCase):
    def test_frenchToEnglish(self):
        self.assertEqual(frenchToEnglish('Bonjour'),('Hello'))
        self.assertNotEqual(frenchToEnglish('Bonjour'),('Bonjour'))

class testMyModuleE(unittest.TestCase):
    def test_englishtoFrench(self):
        self.assertEqual(englishToFrench('Hello'),('Bonjour'))
        self.assertNotEqual(englishToFrench('Hello'),('Hello'))
unittest.main()