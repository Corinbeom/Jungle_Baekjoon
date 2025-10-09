class Solution {
    public String solution(String s) {
        String answer = "";
        int len = s.length();
        int mid = len / 2;
        
        if (len % 2 == 0) {
            answer = "" + s.charAt(mid - 1) + s.charAt(mid);
        } else {
            answer = "" + s.charAt(mid);
        }

        return answer;

    }
}