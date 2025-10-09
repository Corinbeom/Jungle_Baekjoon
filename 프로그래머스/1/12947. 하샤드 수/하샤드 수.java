class Solution {
    public boolean solution(int x) {
        boolean answer = true;
        String[] str = Integer.toString(x).split("");
        
        int harshad = 0;
        
        for (int i = 0; i < str.length; i++) {
            harshad += Integer.parseInt(str[i]);
        }
        
        if (x % harshad == 0) {
            answer = true;
        } else {
            answer = false;
        }
        return answer;
    }
}