import unittest
from core import evaluate
class Tests(unittest.TestCase):
 def test_budget(self):
  r=evaluate(10000,10);self.assertAlmostEqual(r['availability'],.999);self.assertAlmostEqual(r['burn_rate'],1);self.assertFalse(r['alert'])
  self.assertTrue(evaluate(1000,20)['alert'])
 def test_no_data(self):self.assertEqual(evaluate(0,0)['status'],'no-data')
 def test_bounds(self):
  with self.assertRaises(ValueError):evaluate(10,11)
