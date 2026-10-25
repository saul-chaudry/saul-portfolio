using System.Text.RegularExpressions;
var stages=Planner.Create("sample-api","staging","sha256:"+new string('a',64));
if(!stages.SequenceEqual(new[]{"validate","scan","plan","deploy-staging","verify"}))throw new Exception("stage order");
var production=Planner.Create("sample-api","prod","sha256:"+new string('b',64));if(!production.Contains("manual-approval"))throw new Exception("production approval");
try{Planner.Create("sample-api","prod","latest");throw new Exception("mutable image accepted");}catch(ArgumentException){}
Console.WriteLine("PASS: environment validation, immutable artifacts and approval stage");
static class Planner {
 public static string[] Create(string service,string environment,string digest){if(!Regex.IsMatch(service,@"^[a-z][a-z0-9-]{1,40}$")||!new[]{"dev","staging","prod"}.Contains(environment)||!Regex.IsMatch(digest,@"^sha256:[a-f0-9]{64}$"))throw new ArgumentException("invalid deployment input");var stages=new List<string>{"validate","scan","plan"};if(environment=="prod")stages.Add("manual-approval");stages.Add("deploy-"+environment);stages.Add("verify");return stages.ToArray();}
}
