def order(dependencies):
 active=set();done=set();result=[]
 def visit(task):
  if task in done:return
  if task in active:raise ValueError('cycle')
  if task not in dependencies:raise ValueError('missing dependency')
  active.add(task)
  for parent in dependencies[task]:visit(parent)
  active.remove(task);done.add(task);result.append(task)
 for task in dependencies:visit(task)
 return result
def execute(dependencies,handlers,attempts=3):
 if not 1<=attempts<=10:raise ValueError('retry bound')
 schedule=order(dependencies)
 if any(task not in handlers for task in schedule):raise ValueError('missing handler')
 history=[]
 for task in schedule:
  for attempt in range(1,attempts+1):
   try:handlers[task]();history.append((task,attempt,'success'));break
   except Exception:
    history.append((task,attempt,'failed'))
    if attempt==attempts:return {'status':'failed','history':history}
 return {'status':'success','history':history}
