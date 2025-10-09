class Solution {
    public long solution(long n) {
        long sqrt = (long) Math.sqrt(n);
        
        if (sqrt * sqrt == n) {
            return pow(sqrt);
        } else {
            return -1;
        }
    }
    
    public long pow(long x) {
        return (x + 1) * (x + 1);
    }
}