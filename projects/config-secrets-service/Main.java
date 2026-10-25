import java.util.*;
public class Main {
 static void check(boolean condition){if(!condition)throw new AssertionError();}

 record Key(String tenant,String name){}record Revision(int version,String reference){}
 static class Store {
  private final Map<Key,Revision> values=new HashMap<>();private final List<String> audit=new ArrayList<>();
  synchronized Revision put(String tenant,String name,String reference,int expected){if(tenant.isBlank()||name.isBlank()||!reference.matches("vault://[a-zA-Z0-9_/-]+"))throw new IllegalArgumentException("identity or reference");Key key=new Key(tenant,name);Revision old=values.get(key);int version=old==null?0:old.version();if(version!=expected)throw new IllegalStateException("version conflict");Revision next=new Revision(version+1,reference);values.put(key,next);audit.add("updated:"+tenant+":"+name+":"+next.version());return next;}
  synchronized Revision get(String tenant,String name){return values.get(new Key(tenant,name));}
  synchronized List<String> audit(){return List.copyOf(audit);}
 }
 public static void main(String[] args){Store s=new Store();s.put("a","database","vault://apps/db/v1",0);check(s.get("b","database")==null);s.put("a","database","vault://apps/db/v2",1);try{s.put("a","database","vault://apps/db/v3",1);throw new AssertionError();}catch(IllegalStateException expected){}check(s.audit().size()==2);check(s.get("a","database").version()==2);System.out.println("PASS: tenant scope, revision conflicts and reference-only storage");}
}
