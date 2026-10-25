using System.Text.RegularExpressions;
var good=new Evidence("sha256:"+new string('a',64),true,true,0,0);
if(!Gate.Evaluate(good).Allowed||Gate.Evaluate(good with{SignatureVerified=false}).Allowed||Gate.Evaluate(good with{High=1}).Allowed||Gate.Evaluate(good with{Critical=-1}).Allowed)throw new Exception("gate invariant");
Console.WriteLine("PASS: evidence gate fails closed; cryptographic verification remains an adapter");
record Evidence(string Digest,bool SignatureVerified,bool HasSbom,int Critical,int High);
record Decision(bool Allowed,IReadOnlyList<string> Reasons);
static class Gate {
 public static Decision Evaluate(Evidence e){var reasons=new List<string>();if(!Regex.IsMatch(e.Digest,@"^sha256:[a-f0-9]{64}$"))reasons.Add("immutable digest required");if(!e.SignatureVerified)reasons.Add("verified signature required");if(!e.HasSbom)reasons.Add("SBOM required");if(e.Critical!=0||e.High!=0)reasons.Add("nonzero or invalid blocking counts");return new(reasons.Count==0,reasons);}
}
