from pathlib import Path
import re,json
def generate(name,cloud,environment,destination):
 if not re.fullmatch(r'[a-z][a-z0-9-]{1,30}',name) or name.endswith('-'):raise ValueError('name')
 if cloud not in ('aws','azure') or environment not in ('dev','staging','prod'):raise ValueError('target')
 root=Path(destination)/f'{name}-{cloud}-{environment}';root.mkdir(parents=True,exist_ok=False)
 namespace=f'{name}-{environment}'
 resources={'apiVersion':'v1','kind':'Namespace','metadata':{'name':namespace,'labels':{'cloud':cloud,'environment':environment,'pod-security.kubernetes.io/enforce':'restricted'}}}
 (root/'namespace.json').write_text(json.dumps(resources,indent=2))
 (root/'kustomization.yaml').write_text('resources:\n  - namespace.json\n')
 (root/'promotion.json').write_text(json.dumps({'cloud':cloud,'environment':environment,'approval_required':environment=='prod','automatic_pruning':False},indent=2))
 return root
if __name__=='__main__':
 import argparse
 p=argparse.ArgumentParser();p.add_argument('name');p.add_argument('cloud');p.add_argument('environment');p.add_argument('--output',default='artifacts');a=p.parse_args();print(generate(a.name,a.cloud,a.environment,a.output))
