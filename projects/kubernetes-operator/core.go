package operator
import("fmt")
type Spec struct{Name string;Generation int64;Replicas int;Image string}
type Observed struct{Generation int64;Replicas int;Image string;Ready int}
type Decision struct{Action,Condition string;ObservedGeneration int64}
func Reconcile(s Spec,o Observed)(Decision,error){if s.Name==""||s.Generation<1||s.Replicas<1||s.Replicas>100||s.Image==""{return Decision{},fmt.Errorf("invalid spec")};if o.Replicas!=s.Replicas||o.Image!=s.Image{return Decision{"apply","Progressing",s.Generation},nil};if o.Ready!=s.Replicas||o.Generation<s.Generation{return Decision{"requeue","Progressing",o.Generation},nil};return Decision{"none","Ready",s.Generation},nil}
