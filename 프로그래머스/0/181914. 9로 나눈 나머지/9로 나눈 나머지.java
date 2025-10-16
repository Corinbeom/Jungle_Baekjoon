class Solution {
    public int solution(String number) {
        int sum = 0;

        for (int i = 0; i < number.length(); i++) {
            int digit = number.charAt(i) - '0';
            sum = (sum + digit) % 9;
        }

        return sum;
    }
}