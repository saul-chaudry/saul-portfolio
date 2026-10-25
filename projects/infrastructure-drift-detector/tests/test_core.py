import unittest
from core import compare
class Tests(unittest.TestCase):
 def test_allowlisted_diff_and_missing(self):
  d=[{'id':'a','size':1},{'id':'b'}];a=[{'id':'a','size':2,'runtime':'ignored'},{'id':'c'}]
  self.assertEqual([x['kind'] for x in compare(d,a)],['changed','missing','unmanaged'])
 def test_duplicates(self):
  with self.assertRaises(ValueError):compare([{'id':'a'},{'id':'a'}],[])
