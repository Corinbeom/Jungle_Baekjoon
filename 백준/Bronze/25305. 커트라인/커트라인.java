//  커트라인

import java.util.*;
import java.lang.*;
import java.io.*;

class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String[] input = sc.nextLine().split(" ");
        int n = Integer.parseInt(input[0]);
        int k = Integer.parseInt(input[1]);

        Integer score_arr[] = new Integer[n];
        String[] score_input = sc.nextLine().split(" ");
        for (int i = 0; i < n; i++) {
            score_arr[i] = Integer.parseInt(score_input[i]);
        }

        Arrays.sort(score_arr, Collections.reverseOrder());
        System.out.println(score_arr[k-1]);
    }
}