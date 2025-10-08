import java.util.*;

class Solution {
    public ArrayList<Integer> solution(int l, int r) {
        ArrayList<Integer> arr = new ArrayList<>();
        
        for (int i = l; i <= r; i++) {
            String num = String.valueOf(i);
            boolean valid = true;
            for (char c : num.toCharArray()) {
                if (c != '0' && c != '5') {
                    valid = false;
                    break;
                }
            }
            if (valid) {
                arr.add(i);
            }
        }
        if (arr.isEmpty()) {
            arr.add(-1);
        }
        return arr;
    }
}