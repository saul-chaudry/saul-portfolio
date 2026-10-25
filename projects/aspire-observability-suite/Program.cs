using System.Diagnostics;
using var listener=new ActivityListener {ShouldListenTo=s=>s.Name=="Saul.Reference",Sample=(ref ActivityCreationOptions<ActivityContext> options)=>ActivitySamplingResult.AllDataAndRecorded};
ActivitySource.AddActivityListener(listener);using var source=new ActivitySource("Saul.Reference");
using var parent=source.StartActivity("request");using var child=source.StartActivity("database");
if(parent is null||child is null||parent.TraceId!=child.TraceId||child.ParentSpanId!=parent.SpanId)throw new Exception("trace continuity");
Tags.Safe(child,"service.name","reference");Tags.Safe(child,"authorization","secret");Tags.Safe(child,"password","secret");
if(child.GetTagItem("service.name")is null||child.GetTagItem("authorization")is not null)throw new Exception("tag policy");
Console.WriteLine("PASS: trace continuity and tag allowlist");
static class Tags {static readonly HashSet<string> Allowed=new(){"service.name","deployment.environment","db.system","http.request.method"};public static void Safe(Activity activity,string key,string value){if(Allowed.Contains(key))activity.SetTag(key,value);}}
