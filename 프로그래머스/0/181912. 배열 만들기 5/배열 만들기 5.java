import java.util.*;

class Solution {
    public int[] solution(String[] intStrs, int k, int s, int l) {
        ArrayList<Integer> arr = new ArrayList<>();
        for (int i = 0; i < intStrs.length; i++) {
            String str = intStrs[i].substring(s, s + l);
            int num = Integer.parseInt(str);
            
            if (k < num) {
                arr.add(num);
            }
        }
        int[] answer = arr.stream()
                        .mapToInt(i -> i)
                        .toArray();
        
        return answer;
    }
}