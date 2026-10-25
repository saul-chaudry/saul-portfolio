import unittest,tempfile,json
from core import generate
class Tests(unittest.TestCase):
 def test_two_clouds_and_promotion(self):
  with tempfile.TemporaryDirectory() as d:
   for cloud in ('aws','azure'):
    p=generate('demo',cloud,'prod',d);self.assertTrue(json.loads((p/'promotion.json').read_text())['approval_required'])
 def test_validation(self):
  with self.assertRaises(ValueError):generate('../escape','aws','dev','.')
