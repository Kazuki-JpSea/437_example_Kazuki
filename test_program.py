import pdb; pdb.set_trace()
import sys
"""
sys.path.insert(0,/natio/Documents/UW/BIOEN 437 Computational Systems Biology/.Codes/437_example_Kazuki)
"""
from program import hello
import unittest

class TestFunctions(unittest.TestCase):

    def testHello(self):
        result = hello()
        self.assertTrue(result == "Hello")

    def testHell1(self):
        result = hello()
        self.assertTrue(result == "Hello")

if __name__ == '__main__':
  unittest.main()
