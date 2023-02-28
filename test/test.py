import unittest
from fileManager import my_csv as csv
from sort import sort
from operator import itemgetter

class TestStringMethods(unittest.TestCase):

  def test_test(self):
      file = csv.run('../Фильмы.csv')
      compare = lambda a, b: a['Название'] < b['Название']

      self.assertFalse(sort.merge_sort(file, compare) == file)
      self.assertTrue(sort.merge_sort(file, compare) == sorted(file, key=lambda d: d['Название']))

if __name__ == '__main__':
    unittest.main()