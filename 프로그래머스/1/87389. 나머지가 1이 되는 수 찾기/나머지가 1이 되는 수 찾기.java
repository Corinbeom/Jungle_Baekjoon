import java.util.*;

class Solution {
    public int solution(int n) {
        ArrayList<Integer> arr = new ArrayList<>();
        for (int i = 1; i <= n; i++) {
            if (n % i == 1) {
                arr.add(i);
            }
        }
        return arr.get(0);
        
    }
}