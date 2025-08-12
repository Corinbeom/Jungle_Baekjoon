//  팩토리얼 2

import java.util.*;
import java.lang.*;
import java.io.*;

class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int num = Integer.parseInt(sc.nextLine());

        System.out.println(factorial(num));
    }
    static long factorial(int n){
        if (n <= 0){
            return 1;
        }
        return n*factorial(n-1);
    }
}