import unittest
from core import order,execute
class Tests(unittest.TestCase):
 def test_cycle_before_side_effects(self):
  with self.assertRaises(ValueError):order({'a':['b'],'b':['a']})
 def test_order_and_retry(self):
  seen=[]
  def first():
   seen.append('a')
   if len(seen)==1:raise RuntimeError()
  result=execute({'b':['a'],'a':[]},{'a':first,'b':lambda:seen.append('b')},2)
  self.assertEqual(seen,['a','a','b']);self.assertEqual(result['status'],'success')
 def test_stop_on_exhaustion(self):
  def fail():raise RuntimeError()
  self.assertEqual(execute({'a':[],'b':['a']},{'a':fail,'b':lambda:None},2)['history'],[('a',1,'failed'),('a',2,'failed')])
