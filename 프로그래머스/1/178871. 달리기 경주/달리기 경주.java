import java.util.*;

class Solution {
    public String[] solution(String[] players, String[] callings) {
        HashMap<String, Integer> rankMap = new HashMap<>();
        
        for (int i = 0; i < players.length; i++) {
            rankMap.put(players[i], i); 
        }

        for (String call : callings) {
            int idx = rankMap.get(call);   
            if (idx > 0) { 
                String frontPlayer = players[idx - 1];

                players[idx - 1] = call;
                players[idx] = frontPlayer;

                rankMap.put(call, idx - 1);
                rankMap.put(frontPlayer, idx);
            }
        }
        
        return players;
    }
}