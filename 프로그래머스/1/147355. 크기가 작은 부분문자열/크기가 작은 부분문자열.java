class Solution {
    public int solution(String t, String p) {
        int count = 0;
        int len = p.length();
        long target = Long.parseLong(p);
        
        for (int i = 0; i <= t.length() - len; i++) {
            String sub = t.substring(i, i + len);
            long num = Long.parseLong(sub);
            if (num <= target) count++;
        }

        return count;
    }
}