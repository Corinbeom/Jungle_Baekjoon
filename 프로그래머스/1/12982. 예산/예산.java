import java.util.*;

class Solution {
    public int solution(int[] d, int budget) {
        Arrays.sort(d);

        int index = 0;

        while (index < d.length && d[index] <= budget) {
            budget -= d[index++];
        }

        return index;
    }
}