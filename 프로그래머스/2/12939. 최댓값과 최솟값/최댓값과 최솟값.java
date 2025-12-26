import java.util.*;

class Solution {
    public String solution(String s) {
        String answer = "";
        String[] arr = s.split("\\s+");
        int maxNum = Integer.parseInt(arr[0]);
        int minNum = Integer.parseInt(arr[0]);
        
        for (int i = 0; i < arr.length; i++) {
            int cur = Integer.parseInt(arr[i]);
            if (cur < minNum) {
                minNum = cur;
            } else if (cur > maxNum) {
                maxNum = cur;
            }
        }
        answer = minNum + " " + maxNum;
        
        return answer;
    }
}