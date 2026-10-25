package exporter
import("testing";"strings")
func TestStableLabels(t *testing.T){s,e:=Render("queue_depth",map[string]string{"zone":"b","app":"api"},3);if e!=nil||s!="queue_depth{app=\"api\",zone=\"b\"} 3\n"{t.Fatal(s,e)}}
func TestEscapeAndValidate(t *testing.T){s,_:=Render("x",map[string]string{"a":"one\ntwo"},1);if !strings.Contains(s,`one\ntwo`){t.Fatal(s)};if _,e:=Render("bad-name",nil,0);e==nil{t.Fatal("invalid metric accepted")}}
