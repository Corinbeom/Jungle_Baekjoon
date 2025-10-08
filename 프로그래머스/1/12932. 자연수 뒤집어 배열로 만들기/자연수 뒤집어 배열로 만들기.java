class Solution {
    public int[] solution(long n) {
        
        String[] nums = Long.toString(n).split("");
        int[] answer = new int[nums.length];
        
        int j = 0;
        for (int i = nums.length - 1; i >= 0; i--) {
            answer[j++] = Integer.parseInt(nums[i]);
        }
        return answer;
    }
}