class Solution {
    public String solution(String my_string, int[][] queries) {
        StringBuilder sb = new StringBuilder(my_string);
        
        for (int[] q : queries) {
            int s = q[0];
            int e = q[1];
            
            String reverse = new StringBuilder(sb.substring(s, e + 1))
                .reverse()
                .toString();
            
            sb.replace(s, e + 1, reverse);
        }
        
        return sb.toString();
    }
}