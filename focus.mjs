export const paths={fullstack:'Full Stack',java:'Java',dotnet:'.NET',python:'Python',go:'Go',devops:'DevOps'};
export function normalize(search){const key=new URLSearchParams(search).get('focus');return key==='all'||paths[key]?key:'selected'}
export function select(projects,focus,query=''){const q=query.trim().toLowerCase();if(focus==='selected'&&!q)return Object.values(paths).map(group=>projects.find(p=>p.group===group)).filter(Boolean);return projects.filter(p=>(!paths[focus]||p.group===paths[focus])&&[p.title,p.implemented,p.stack].join(' ').toLowerCase().includes(q))}
export function url(focus){return focus==='selected'?'?':'?focus='+focus}
