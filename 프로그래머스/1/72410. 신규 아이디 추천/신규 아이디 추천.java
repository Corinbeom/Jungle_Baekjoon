class Solution {
    public String solution(String new_id) {
        
        String special_char = "[^a-z0-9._-]";
        
        String res_id = "a";
        
        if (new_id.isEmpty()) {
            res_id = "aaa";
        } else {
            res_id = new_id;
        }
        

        

        res_id = res_id.toLowerCase();

        res_id = res_id.replaceAll(special_char, "");

        if (res_id.contains("..")) {
            res_id = res_id.replaceAll("\\.{2,}", ".");
        }

        res_id = res_id.replaceAll("^\\.|\\.$", "");
        
        if (res_id.isEmpty()) {
            res_id = "a";
        }

        if (res_id.length() > 15) {
            res_id = res_id.substring(0, 15);
        } else if (res_id.length() < 3) {
            String add_char = res_id.substring(res_id.length() - 1);
            while (res_id.length() < 3) {
                res_id += add_char;
            }
        }
        res_id = res_id.replaceAll("^\\.|\\.$", "");
        
        return res_id;
    }
}