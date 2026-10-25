from copy import deepcopy
def compare(desired,actual,managed=('size','region','tags')):
 d={r['id']:r for r in desired};a={r['id']:r for r in actual}
 if len(d)!=len(desired) or len(a)!=len(actual):raise ValueError('duplicate identity')
 changes=[]
 for key in sorted(d.keys()|a.keys()):
  if key not in a:changes.append({'id':key,'kind':'missing'});continue
  if key not in d:changes.append({'id':key,'kind':'unmanaged'});continue
  for field in managed:
   if d[key].get(field)!=a[key].get(field):changes.append({'id':key,'kind':'changed','field':field,'desired':deepcopy(d[key].get(field)),'actual':deepcopy(a[key].get(field))})
 return changes
