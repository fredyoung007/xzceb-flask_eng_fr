#!/usr/bin/env python3
"""tests.py
"""

import unittest
from translator import english_to_french as e2f, french_to_english as f2e

class TranslatorTest(unittest.TestCase):
    def setUp(self):
        self.english = "Hello"
        self.french = "Bonjour"

    def testNullE2F(self):
        self.assertIsNone(f2e(None))

    def testTransE2F(self):
        self.assertEqual(e2f(self.english), self.french)
    
    def testNullF2E(self):
        self.assertIsNone(e2f(None))
    
    def testTransF2E(self):
        self.assertEqual(f2e(self.french), self.english)

if __name__ == "__main__":
    unittest.main()