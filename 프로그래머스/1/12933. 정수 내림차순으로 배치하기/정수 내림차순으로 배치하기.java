import java.util.*;

class Solution {
    public long solution(long n) {
        String[] nums = Long.toString(n).split("");
        Arrays.sort(nums, Collections.reverseOrder());
        String str = String.join("",nums);
        long result = Long.parseLong(str);
        
        return result;
    }
}