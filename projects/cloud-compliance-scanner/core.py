def scan(resources):
 findings=[]
 for r in resources:
  if not r.get('id') or not r.get('kind'):raise ValueError('resource identity required')
  if r['kind']=='s3' and r.get('public') is True:findings.append((r['id'],'public-storage'))
  if r['kind']=='iam' and ('*' in r.get('actions',[]) or '*' in r.get('resources',[])):findings.append((r['id'],'wildcard-permission'))
  if r['kind']=='security-group':
   for rule in r.get('ingress',[]):
    if rule.get('cidr') in ('0.0.0.0/0','::/0') and rule.get('port') in (22,3389):findings.append((r['id'],'public-administration-port'))
 return sorted(set(findings))
