def evaluate(total,failed,target=0.999,burn_threshold=14.4):
 if not isinstance(total,int) or not isinstance(failed,int) or not 0<=failed<=total or not 0<target<1 or burn_threshold<=0:raise ValueError('invalid SLO input')
 if total==0:return {'status':'no-data','availability':None,'burn_rate':None,'alert':False}
 error_ratio=failed/total;allowed=1-target;burn=error_ratio/allowed
 return {'status':'measured-window','availability':1-error_ratio,'burn_rate':burn,'budget_remaining_fraction':1-burn,'alert':burn>=burn_threshold}
