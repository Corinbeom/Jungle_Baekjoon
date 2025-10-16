class Solution {
    public boolean solution(boolean x1, boolean x2, boolean x3, boolean x4) {
        boolean answer = true;
        boolean x1x2 = (x1 == true || x2 == true) ? true : false;
        boolean x3x4 = (x3 == true || x4 == true) ? true : false;
        answer = (x1x2 == true && x3x4 == true) ? true : false;
        return answer;
    }
}