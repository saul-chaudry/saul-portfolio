import java.util.*;
public class Main {
 static void check(boolean condition){if(!condition)throw new AssertionError();}

 static int replicas(int current,double utilization,double target,int min,int max){if(current<1||min<1||max<min||!Double.isFinite(utilization)||utilization<0||!Double.isFinite(target)||target<=0)throw new IllegalArgumentException();return (int)Math.max(min,Math.min(max,Math.ceil(current*utilization/target)));}
 static boolean promote(int requests,int errors,double p95,double maxLatency){if(requests<=0||errors<0||errors>requests||!Double.isFinite(p95)||p95<0||maxLatency<=0)return false;return (double)errors/requests<=0.01&&p95<=maxLatency;}
 public static void main(String[] args){check(replicas(3,.9,.6,2,8)==5);check(replicas(3,0,.6,2,8)==2);check(replicas(3,8,.6,2,8)==8);check(promote(1000,5,100,200));check(!promote(100,10,100,200));check(!promote(0,0,0,200));System.out.println("PASS: scaling bounds and canary gates");}
}
