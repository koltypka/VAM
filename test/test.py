import unittest

class TestStringMethods(unittest.TestCase):

  def test_test(self):
      self.assertTrue([1,2,3] == [1,2,3])
      self.assertFalse([1,2,3] == dict('test'))

if __name__ == '__main__':
    unittest.main()