import java.util.*;

class Solution {
    
    ArrayList<int[]> seq;
    public int[][] solution(int n) {
        seq = new ArrayList<>();
        
        hanoi(n, 1, 3, 2);
        
        int[][] answer = new int[seq.size()][2];
        
        for (int i = 0; i <seq.size(); ++i) {
            int[] cmd = seq.get(i);
            answer[i][0] = cmd[0];
            answer[i][1] = cmd[1];
        }
        return answer;
    }
    
    public void hanoi(int n, int start, int end, int mid) {
        int[] move = {start, end};
        
        if (n == 1) {
            seq.add(move);
        } else {
            hanoi(n - 1, start, mid, end);
            seq.add(move);
            hanoi(n - 1, mid, end, start);
        }
    }
}