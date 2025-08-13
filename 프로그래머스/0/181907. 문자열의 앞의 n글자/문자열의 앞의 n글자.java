import java.util.*;

class Solution {
    public String solution(String my_string, int n) {
        StringBuilder answer_str = new StringBuilder();
        
        for (int i = 0; i < n; i++) {
            answer_str.append(my_string.charAt(i));
        }
        
        return answer_str.toString();
    
    }
}