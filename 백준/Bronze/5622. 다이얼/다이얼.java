//  다이얼

import java.util.*;
import java.lang.*;
import java.io.*;

class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String words = sc.nextLine();
        char[] wordArray = words.toCharArray();
        int count = 0;

        for (int i = 0; i < words.length(); i++) {
            if (wordArray[i] == 'A' || wordArray[i] == 'B' || wordArray[i] == 'C') {
                count += 3;
            } else if (wordArray[i] == 'D' || wordArray[i] == 'E' || wordArray[i] == 'F') {
                count += 4;
            } else if (wordArray[i] == 'G' || wordArray[i] == 'H' || wordArray[i] == 'I') {
                count += 5;
            } else if (wordArray[i] == 'J' || wordArray[i] == 'K' || wordArray[i] == 'L') {
                count += 6;
            } else if (wordArray[i] == 'M' || wordArray[i] == 'N' || wordArray[i] == 'O') {
                count += 7;
            } else if (wordArray[i] == 'P' || wordArray[i] == 'Q' || wordArray[i] == 'R' || wordArray[i] == 'S') {
                count += 8;
            } else if (wordArray[i] == 'T' || wordArray[i] == 'U' || wordArray[i] == 'V') {
                count += 9;
            } else if (wordArray[i] == 'W' || wordArray[i] == 'X' || wordArray[i] == 'Y' || wordArray[i] == 'Z') {
                count += 10;
            }
        }
        System.out.println(count);
    }
}