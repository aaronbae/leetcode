// you can also use imports, for example:
import java.util.*;

// you can write to stdout for debugging purposes, e.g.
// System.out.println("this is a debug message");

class Solution {
    public int recurse(Tree current, int prevMax){
        if(current == null){
              return 0;
        }
        int result = 0;
        if(prevMax <= current.x){
              result += 1;
        }
        result += recurse(current.l, Math.max(prevMax, current.x));
        result += recurse(current.r, Math.max(prevMax, current.x));
        return result;
    }

    public int solution(Tree T) {
        // write your code in Java SE 8
        return recurse(T, -100000);
    }
}
