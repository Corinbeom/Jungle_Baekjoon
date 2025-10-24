import java.util.*;

class Solution {
    
    int answer = 0; 

    public void dfs(int[] numbers, int index, int sum, int target) {
        if (index == numbers.length) { // 모든 숫자를 다 사용했을 때
            if (sum == target) answer++;
            return;
        }

        // 현재 숫자를 +로 더하는 경우
        dfs(numbers, index + 1, sum + numbers[index], target);

        // 현재 숫자를 -로 빼는 경우
        dfs(numbers, index + 1, sum - numbers[index], target);
    }

    public int solution(int[] numbers, int target) {
        dfs(numbers, 0, 0, target);
        return answer;
    }
}