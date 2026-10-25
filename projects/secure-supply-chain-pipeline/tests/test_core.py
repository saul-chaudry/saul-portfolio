import unittest
from core import decide
class Tests(unittest.TestCase):
 def test_deny_by_default(self):self.assertFalse(decide({})['allowed'])
 def test_positive_and_negative_evidence(self):
  e={'digest':'sha256:'+'a'*64,'signature_verified':True,'sbom':'fixture','vulnerabilities':{'critical':0,'high':0}}
  self.assertTrue(decide(e)['allowed']);e['vulnerabilities']['high']=1;self.assertFalse(decide(e)['allowed'])
