class Solution {
    boolean solution(String s) {
        boolean answer = true;
        s = s.toLowerCase();
        String[] str = s.split("");
        int pCnt = 0;
        int yCnt = 0;
        
        for (int i = 0; i < str.length; i++) {
            if (str[i].equals("p")) {
                pCnt += 1;
            } else if (str[i].equals("y")) {
                yCnt += 1;
            } else {
                continue;
            }
        }

        if (pCnt == yCnt) {
            answer = true;
        } else {
            answer = false;
        }
        return answer;
    }
}