class Solution {
    public int solution(int num1, int num2) {
        double temp = (double)num1 / (double)num2;
        temp = temp * 1000;
        int result = (int)Math.floor(temp);
        
        return result;
    }
}