package exporter
import("fmt";"regexp";"sort";"strconv";"strings";"math")
var name=regexp.MustCompile(`^[a-zA-Z_][a-zA-Z0-9_]*$`)
func Render(metric string,labels map[string]string,value float64)(string,error){if !name.MatchString(metric)||math.IsNaN(value)||math.IsInf(value,0){return "",fmt.Errorf("invalid metric")};keys:=[]string{};for k:=range labels{if !name.MatchString(k){return "",fmt.Errorf("invalid label")};keys=append(keys,k)};sort.Strings(keys);parts:=[]string{};for _,k:=range keys{v:=strings.NewReplacer(`\`,`\\`,"\n",`\n`,`"`,`\"`).Replace(labels[k]);parts=append(parts,k+`="`+v+`"`)};suffix:="";if len(parts)>0{suffix="{"+strings.Join(parts,",")+"}"};return metric+suffix+" "+strconv.FormatFloat(value,'g',-1,64)+"\n",nil}
