//  대표값2

import java.util.*;
import java.lang.*;
import java.io.*;
import java.math.*;

class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int[] num_array = new int[5];
        for (int i = 0; i < 5; i++) {
            int num = sc.nextInt();
            num_array[i] = num;
        }
        int aver = Arrays.stream(num_array).sum() / num_array.length;
        Arrays.sort(num_array);
        int middle = num_array[ num_array.length / 2 ];
        System.out.println(aver);
        System.out.println(middle);
    }
}