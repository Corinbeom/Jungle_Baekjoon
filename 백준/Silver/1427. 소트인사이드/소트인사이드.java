//  소트인사이드

import java.util.*;
import java.lang.*;
import java.io.*;

class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String nums = sc.nextLine();
        char[] num = nums.toCharArray();
        int[] result = new int[num.length];

        for (int i = 0; i < num.length; i++) {
            result[i] = Integer.parseInt(String.valueOf(num[i]));
        }
        Arrays.sort(result);

        for (int j = result.length -1; j >= 0; j--) {
            System.out.print((result[j]));
        }
    }
}