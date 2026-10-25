package operator
import "testing"
func TestReconcile(t *testing.T){s:=Spec{"api",2,3,"digest"};d,_:=Reconcile(s,Observed{});if d.Action!="apply"{t.Fatal(d)};d,_=Reconcile(s,Observed{2,3,"digest",2});if d.Action!="requeue"{t.Fatal(d)};d,_=Reconcile(s,Observed{2,3,"digest",3});if d.Condition!="Ready"{t.Fatal(d)}}
func TestInvalid(t *testing.T){if _,err:=Reconcile(Spec{},Observed{});err==nil{t.Fatal("invalid spec accepted")}}
