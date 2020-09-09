// you can also use imports, for example:
import java.util.*;
import java.lang.*;

// you can write to stdout for debugging purposes, e.g.
// System.out.println("this is a debug message");

class Solution {
    public static class Tuple implements Comparable<Tuple> {
      public int index;
      public int value;
      public Tuple(int index, int value) {
        this.index = index;
        this.value = value;
      }
      public int compareTo(Tuple other) {
        return this.value - other.value;
      }
      public String toString(){
        return "["+this.index+","+this.value+"]";
      }
    }
    public int solution(int[] A) {
        // write your code in Java SE 8
        Tuple[] tuplifiedArray = new Tuple[A.length];
        for(int i = 0; i < A.length; i++){
          tuplifiedArray[i] = new Tuple(i, A[i]);
        }
        Arrays.sort(tuplifiedArray);

        int best = 40000;
        Tuple prevForward = new Tuple(-80000, -2147483648);
        Tuple prevBackward = new Tuple(80000, -2147483648);
        for(int i = 0; i < A.length; i++){
          Tuple forward = tuplifiedArray[i];
          Tuple backward = tuplifiedArray[A.length - 1 - i];
          
          if(prevForward.value != forward.value){
            if(Math.abs(forward.index-prevForward.index) < best ){
              best = Math.abs(forward.index-prevForward.index);
            }
            prevForward = forward;
          }
          if(prevBackward.value != backward.value){
            if(Math.abs(backward.index-prevBackward.index) < best ){
              best = Math.abs(backward.index-prevBackward.index);
            }
            prevBackward = backward;
          }
        }
        return best;
    }
    public static void main(String[] args){
        Solution a = new Solution();
        int[] shit = {1,4,7,3,3,5};
        System.out.println(a.solution(shit));
    }
}

