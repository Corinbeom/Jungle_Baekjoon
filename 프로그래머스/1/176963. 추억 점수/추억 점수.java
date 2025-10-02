import java.util.*;

class Solution {
    public ArrayList<Integer> solution(String[] name, int[] yearning, String[][] photo) {
        Map<String, Integer> map = new HashMap<>();
        for (int i = 0; i < name.length; i++) {
            map.put(name[i], yearning[i]);
        }
        ArrayList<Integer> result = new ArrayList<>();
        
        for (int i = 0; i < photo.length; i++) {
            int sum = 0;
            for (int j = 0; j < photo[i].length; j++){
                if (map.get(photo[i][j]) != null) {
                    sum += map.get(photo[i][j]);
                }
            }
            result.add(sum);
        }
        return result;
    }
}