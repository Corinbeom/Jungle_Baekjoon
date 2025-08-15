import java.util.*;
class Solution {
    public String solution(String X, String Y) {
        int[] countX = new int[10];
        int[] countY = new int[10];
        
        // X, Y 각 숫자 개수 세기
        for (int i = 0; i < X.length(); i++) {
            countX[X.charAt(i) - '0']++;
        }
        for (int i = 0; i < Y.length(); i++) {
            countY[Y.charAt(i) - '0']++;
        }
        
        StringBuilder sb = new StringBuilder();
        
        // 9부터 0까지 (큰 수부터) - 정렬 불필요
        for (int i = 9; i >= 0; i--) {
            int commonCount = Math.min(countX[i], countY[i]);
            for (int j = 0; j < commonCount; j++) {
                sb.append(i);
            }
        }
        
        if (sb.length() == 0) {
            return "-1";
        }
        if (sb.charAt(0) == '0') {
            return "0";
        }
        
        return sb.toString();
    }
}