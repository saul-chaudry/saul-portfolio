package verify
import("testing";"net/http";"net/http/httptest";"context";"time")
func TestHealthAndOrder(t *testing.T){server:=httptest.NewServer(http.HandlerFunc(func(w http.ResponseWriter,r *http.Request){if r.URL.Path=="/bad"{w.WriteHeader(503)}}));defer server.Close();results,e:=Check(context.Background(),[]string{server.URL,server.URL+"/bad"},2,&http.Client{Timeout:time.Second});if e!=nil||!results[0].Healthy||results[1].Healthy{t.Fatal(results,e)}}
func TestCancellation(t *testing.T){ctx,cancel:=context.WithCancel(context.Background());cancel();_,e:=Check(ctx,[]string{"http://127.0.0.1:1"},1,&http.Client{Timeout:time.Second});if e==nil{t.Fatal("missing cancellation")}}
