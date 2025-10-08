import java.util.*;

class Solution {
    public int solution(int num) {
        
        ArrayList<Integer> arr = new ArrayList<>();
        int count = 0;
        
        while (num != 1) {
            if (num % 2 == 0) {
                arr.add(num);
                num = num / 2;
            } else if (num % 2 == 1) {
                arr.add(num);
                num = num * 3 + 1;
            }
            
            count++;
            
            if (count == 500) return -1;
        }
        
        return arr.size();
        
    }
}