import java.io.*;
import java.util.*;
import java.util.stream.*;
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
    public static int gcdOfList(List<Integer> numbers) {
        int result = numbers.get(0);
        for (int i = 1; i < numbers.size(); i++) {
            result = gcd(result, numbers.get(i));
        }
        return result;
    }

    // Computes the LCM of a list
    public static int lcmOfList(List<Integer> numbers) {
        int result = numbers.get(0);
        for (int i = 1; i < numbers.size(); i++) {
            result = lcm(result, numbers.get(i));
        }
        return result;
    }

    public static int getTotalX(List<Integer> a, List<Integer> b) {
        int lcmA = lcmOfList(a);
        int gcdB = gcdOfList(b);
        int count = 0;

        for (int num = lcmA; num <= gcdB; num += lcmA) {
            if (gcdB % num == 0) {
                count++;
            }
        }

        return count;
    }
}

public class Data13 {

    public static void main(String[] args) throws IOException {
        BufferedReader reader = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter writer = new BufferedWriter(
                new FileWriter(System.getenv("OUTPUT_PATH")));

        String[] firstLine = reader.readLine().trim().split(" ");
        int n = Integer.parseInt(firstLine[0]);
        int m = Integer.parseInt(firstLine[1]);

        List<Integer> a = Stream.of(reader.readLine().trim().split(" "))
                .map(Integer::parseInt)
                .collect(toList());

        List<Integer> b = Stream.of(reader.readLine().trim().split(" "))
                .map(Integer::parseInt)
                .collect(toList());

        int total = Result.getTotalX(a, b);

        writer.write(String.valueOf(total));
        writer.newLine();

        reader.close();
        writer.close();
    }
}
