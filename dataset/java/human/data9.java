import java.io.*;
import java.math.*;
import java.security.*;
import java.text.*;
import java.util.*;
import java.util.concurrent.*;
import java.util.function.*;
import java.util.regex.*;
import java.util.stream.*;
import static java.util.stream.Collectors.joining;
import static java.util.stream.Collectors.toList;

class Result {
    public static void separateNumbers(String s) {
        for (int i = 1, n = s.length(); i <= n / 2; i++) {
            // Compute the first number based on the first 'i' characters of string 's'
            String firstNumStr = s.substring(0, i);
            long firstNum = Long.parseLong(firstNumStr);
            StringBuilder beautifulStr = new StringBuilder(firstNumStr);

            // Build a beautiful string starting with 'firstNum'
            long nextNum = firstNum;
            while (beautifulStr.length() < n) {
                nextNum++;
                beautifulStr.append(nextNum);
            }

            // If the newly created beautiful string equals 's' we have a match
            if (beautifulStr.toString().equals(s)) {
                System.out.println("YES " + firstNumStr);
                return;
            }
        }

        System.out.println("NO");
    }
}

public class Data9 {
    public static void main(String[] args) throws IOException {
        BufferedReader bufferedReader = new BufferedReader(new InputStreamReader(System.in));

        int q = Integer.parseInt(bufferedReader.readLine().trim());

        IntStream.range(0, q).forEach(qItr -> {
            try {
                String s = bufferedReader.readLine();

                Result.separateNumbers(s);
            } catch (IOException ex) {
                throw new RuntimeException(ex);
            }
        });

        bufferedReader.close();
    }
}