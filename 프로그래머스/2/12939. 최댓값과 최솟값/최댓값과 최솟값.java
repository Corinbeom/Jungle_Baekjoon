import java.util.*;

class Solution {
    public String solution(String s) {
        String[] nums = s.split(" ");
        int n = nums.length;
        int[] arr = new int[n];
        
        for (int i = 0; i < n; i++) {
            arr[i] = Integer.parseInt(nums[i]);
        }
        int maxNum = Arrays.stream(arr).max().getAsInt();
        int minNum = Arrays.stream(arr).min().getAsInt();
        
        String maxStr = Integer.toString(maxNum);
        String minStr = Integer.toString(minNum);
        String res = minStr+" "+maxStr;
        return res;
    }
}