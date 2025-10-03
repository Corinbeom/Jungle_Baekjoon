import java.util.*;

class Solution {
    public int[] solution(String[] id_list, String[] report, int k) {
        int[] answer = new int[id_list.length];
        
        Set<String> report_set = new HashSet<>(Arrays.asList(report));
        
        Map<String, Integer> report_count = new HashMap<>();
        for (String r : report_set) {
            String[] users = r.split(" ");
            String reported = users[1];
            report_count.put(reported, report_count.getOrDefault(reported, 0) + 1);
        }
        
        Set<String> ban_list = new HashSet<>();
        for (String user : report_count.keySet()) {
            if (report_count.get(user) >= k) {
                ban_list.add(user);
            }
        }
        
        for (String r : report_set) {
            String[] user = r.split(" ");
            String reporter = user[0];
            String reported = user[1];
            
            if (ban_list.contains(reported)) {
                int idx = Arrays.asList(id_list).indexOf(reporter);
                answer[idx]++; 
            }
        }
        return answer;
    }
}
