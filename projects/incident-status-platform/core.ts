type Stage='investigating'|'identified'|'monitoring'|'resolved';
export class Incident{
 private stage:Stage='investigating';private escalation=0;private deadline:number;private interval:number;private updates:{stage:Stage,message:string}[]=[];
 constructor(now:number,interval:number){if(!Number.isFinite(now)||interval<=0||!Number.isFinite(interval))throw Error('time');this.interval=interval;this.deadline=now+interval}
 update(to:Stage,publicMessage:string){const order:Stage[]=['investigating','identified','monitoring','resolved'];if(order.indexOf(to)!==order.indexOf(this.stage)+1||!publicMessage.trim())throw Error('invalid update');this.stage=to;this.updates.push({stage:to,message:publicMessage})}
 tick(now:number){if(this.stage!=='resolved'&&now>=this.deadline){this.escalation++;this.deadline=now+this.interval;return true}return false}
 publicStatus(){return {stage:this.stage,updates:this.updates.map(x=>({...x}))}}
 escalationLevel(){return this.escalation}
}
