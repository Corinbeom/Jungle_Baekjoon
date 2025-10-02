//  균형잡힌 세상

import java.util.*;
import java.lang.*;
import java.io.*;

class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder sb = new StringBuilder();


        while (true) {
            String line = br.readLine();
            if (line.equals(".")) break;  // 입력 종료 조건
            sb.append(stacklogic(line)).append("\n");

        }

        System.out.println(sb);
    }

    public static String stacklogic(String str) {
        Stack<Character> st = new Stack<>();

        for (int i = 0; i < str.length(); i++) {
            char c = str.charAt(i);
            if (c == '(' || c == '[') {
                st.push(c);
            }
            else if (c == ')') {
                if (st.isEmpty() || st.peek() != '(') {
                    return "no";
                } else {
                    st.pop();
                }
            } else if (c == ']') {
                if (st.isEmpty() || st.peek() != '[') {
                    return "no";
                } else {
                    st.pop();
                }
            }
        }
        if (st.isEmpty()) {
            return "yes";
        } else {
            return "no";
        }
    }
}