import java.util.*;
public class Main {
 static void check(boolean condition){if(!condition)throw new AssertionError();}

 static class Breaker {
  final int threshold;final long cooldown;int failures=0;long reopen=0;String state="closed";boolean probe=false;
  Breaker(int threshold,long cooldown){if(threshold<1||cooldown<1)throw new IllegalArgumentException();this.threshold=threshold;this.cooldown=cooldown;}
  synchronized boolean acquire(long now){if(state.equals("open")){if(now<reopen)return false;state="half-open";}if(state.equals("half-open")){if(probe)return false;probe=true;}return true;}
  synchronized void result(boolean success,long now){if(state.equals("half-open")){probe=false;if(success){state="closed";failures=0;}else{state="open";reopen=now+cooldown;}return;}if(!state.equals("closed"))return;if(success)failures=0;else if(++failures>=threshold){state="open";reopen=now+cooldown;}}
 }
 public static void main(String[] args){Breaker b=new Breaker(2,10);check(b.acquire(0));b.result(false,0);check(b.acquire(1));b.result(false,1);check(!b.acquire(10));check(b.acquire(11));check(!b.acquire(11));b.result(true,12);check(b.state.equals("closed"));check(b.acquire(12));System.out.println("PASS: open, cooldown, exclusive half-open probe and recovery");}
}
