import java.util.*;

class Solution {
    public int[] solution(String s) {
        int[] answer = new int[s.length()];

        HashMap<Character, Integer> lastIdx = new HashMap<>();
        
        for (int i = 0; i < s.length(); i++) {
            char c = s.charAt(i);
            if (!lastIdx.containsKey(c)) {
                answer[i] = -1;
            } else if (lastIdx.containsKey(c)) {
                answer[i] = i - lastIdx.get(c);
            }
            lastIdx.put(c, i);
        }
        return answer;
    }
}