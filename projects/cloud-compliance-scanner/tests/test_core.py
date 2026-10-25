import unittest
from core import scan
class Tests(unittest.TestCase):
 def test_policies(self):
  data=[{'id':'bucket','kind':'s3','public':True},{'id':'role','kind':'iam','actions':['*']},{'id':'sg','kind':'security-group','ingress':[{'cidr':'::/0','port':22}]}]
  self.assertEqual(len(scan(data)),3);self.assertEqual(scan([{'id':'private','kind':'s3','public':False}]),[])
 def test_invalid_identity(self):
  with self.assertRaises(ValueError):scan([{'kind':'s3'}])
