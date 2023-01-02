import unittest
from translator import frenchToEnglish, englishToFrench

class testMyModuleF(unittest.TestCase):
    def test_frenchToEnglish(self):
        self.assertEqual(frenchToEnglish('bonjour'),('hello'))
        self.assertNotEqual(frenchToEnglish('bonjour'),('bonjour'))

class testMyModuleE(unittest.TestCase):
    def test_englishtoFrench(self):
        self.assertEqual(englishToFrench('hello'),('bounjour'))
        self.assertNotEqual(englishToFrench('hello'),('hello'))
unittest.main()