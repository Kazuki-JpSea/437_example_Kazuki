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
