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
    // Computes the GCD of two numbers
    public static int gcd(int a, int b) {
        while (a != b) {
            if (a > b) {
                a -= b;
            } else {
                b -= a;
            }
        }

        return a;
    }

    // Computes the LCM of two numbers
    public static int lcm(int a, int b) {
        return Math.abs(a * b) / gcd(a, b);
    }

    // Computes the GCD of a list
    public static int gcdOfList(List<Integer> list) {
        int result = list.get(0);

        for (int i = 1, n = list.size(); i < n; i++) {
            result = gcd(result, list.get(i));
        }

        return result;
    }

    // Computes the LCM of a list
    public static int lcmOfList(List<Integer> list) {
        int result = list.get(0);

        for (int i = 1, n = list.size(); i < n; i++) {
            result = lcm(result, list.get(i));
        }

        return result;
    }

    public static int getTotalX(List<Integer> a, List<Integer> b) {
        int lcmOfA = lcmOfList(a);
        int gcdOfB = gcdOfList(b);
        int count = 0;

        for (int num = lcmOfA; num <= gcdOfB; num += lcmOfA) {
            if (gcdOfB % num == 0) {
                count++;
            }
        }

        return count;
    }
}

public class Data13 {
    public static void main(String[] args) throws IOException {
        BufferedReader bufferedReader = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bufferedWriter = new BufferedWriter(new FileWriter(System.getenv("OUTPUT_PATH")));

        String[] firstMultipleInput = bufferedReader.readLine().replaceAll("\\s+$", "").split(" ");

        int n = Integer.parseInt(firstMultipleInput[0]);

        int m = Integer.parseInt(firstMultipleInput[1]);

        List<Integer> arr = Stream.of(bufferedReader.readLine().replaceAll("\\s+$", "").split(" "))
                .map(Integer::parseInt)
                .collect(toList());

        List<Integer> brr = Stream.of(bufferedReader.readLine().replaceAll("\\s+$", "").split(" "))
                .map(Integer::parseInt)
                .collect(toList());

        int total = Result.getTotalX(arr, brr);

        bufferedWriter.write(String.valueOf(total));
        bufferedWriter.newLine();

        bufferedReader.close();
        bufferedWriter.close();
    }
}