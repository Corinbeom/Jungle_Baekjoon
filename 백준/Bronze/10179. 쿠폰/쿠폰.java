import java.util.*;
import java.lang.*;
import java.io.*;

class Main {
    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int tc = Integer.parseInt(br.readLine());
        double[] prices = new double[tc];
        for (int i = 0; i < tc; i++) {
            prices[i] = Double.parseDouble(br.readLine());
        }
        StringBuilder sb = new StringBuilder();

        for (int i = 0; i < tc; i++) {
            prices[i] *= 0.8;
            String result = String.format("%.2f", prices[i]);
            sb.append("$").append(result).append("\n");
        }
        System.out.println(sb);
    }
}