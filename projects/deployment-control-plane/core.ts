type Role='reader'|'operator';type State='pending'|'deploying'|'healthy'|'rolled-back';
export class ControlPlane{
 private state:State='pending';private version=0;private audit:{actor:string,from:State,to:State,version:number}[]=[];
 transition(actor:string,role:Role,to:State,expected:number){if(!actor||role!=='operator')throw Error('forbidden');if(expected!==this.version)throw Error('version conflict');const allowed:Record<State,State[]>={'pending':['deploying'],'deploying':['healthy','rolled-back'],'healthy':['rolled-back'],'rolled-back':[]};if(!allowed[this.state].includes(to))throw Error('invalid transition');const from=this.state;this.state=to;this.version++;this.audit.push({actor,from,to,version:this.version});return this.snapshot()}
 snapshot(){return {state:this.state,version:this.version,audit:this.audit.map(x=>({...x}))}}
}
