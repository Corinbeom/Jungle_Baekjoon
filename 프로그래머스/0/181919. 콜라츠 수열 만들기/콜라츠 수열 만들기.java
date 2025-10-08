import java.util.*;

class Solution {
    public ArrayList<Integer> solution(int n) {
        ArrayList<Integer> list = new ArrayList<>();
        list.add(n);
        while (n != 1) {
            int temp = 0;
            if (n % 2 == 0) {
                temp = n / 2;
                list.add(temp);
                n = temp;
            } else {
                temp = 3 * n + 1;
                list.add(temp);
                n = temp;
            }
        }
        return list;
    }
}