import re
def decide(evidence):
 reasons=[]
 if not re.fullmatch(r'sha256:[a-f0-9]{64}',evidence.get('digest','')):reasons.append('immutable digest required')
 if evidence.get('signature_verified') is not True:reasons.append('verified signature required')
 if not evidence.get('sbom'):reasons.append('SBOM required')
 counts=evidence.get('vulnerabilities',{})
 if any(not isinstance(counts.get(k),int) or isinstance(counts.get(k),bool) or counts[k]<0 for k in ('critical','high')):reasons.append('valid complete vulnerability counts required')
 elif counts['critical'] or counts['high']:reasons.append('blocking vulnerabilities')
 return {'allowed':not reasons,'reasons':reasons,'scope':'supplied evidence only; not a signature verifier'}
