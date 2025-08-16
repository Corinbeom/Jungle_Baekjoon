import java.util.*;

class Solution {
    public String[] solution(String[] record) {
        Map<String, String> userMap = new HashMap<>();
        
        Arrays.stream(record)
            .map(r -> r.split(" "))
            .filter(parts -> !"Leave".equals(parts[0]))
            .forEach(parts -> userMap.put(parts[1], parts[2]));
        
        return Arrays.stream(record)
            .map(r -> r.split(" "))
            .filter(parts -> !"Change".equals(parts[0]))
            .map(parts -> userMap.get(parts[1]) + 
                 ("Enter".equals(parts[0]) ? "님이 들어왔습니다." : "님이 나갔습니다."))
            .toArray(String[]::new);
    }
}