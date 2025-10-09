import java.util.*;

class Solution {
    public String solution(String phone_number) {
        int len = phone_number.length();  
        String last4 = phone_number.substring(len - 4);  
        String masked = "*".repeat(len - 4); 
        return masked + last4;
    }
}