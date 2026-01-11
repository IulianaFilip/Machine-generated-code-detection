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
    public static int marsExploration(String s) {
        int count = 0;

        for (int i = 0, n = s.length(); i < n; i++) {
            char ch = s.charAt(i);

            if (i % 3 == 0 || i % 3 == 2) {
                if (ch != 'S') {
                    count++;
                }
            } else {
                if (ch != 'O') {
                    count++;
                }
            }
        }

        return count;
    }
}

public class Data20 {
    public static void main(String[] args) throws IOException {
        BufferedReader bufferedReader = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bufferedWriter = new BufferedWriter(new FileWriter(System.getenv("OUTPUT_PATH")));

        String s = bufferedReader.readLine();

        int result = Result.marsExploration(s);

        bufferedWriter.write(String.valueOf(result));
        bufferedWriter.newLine();

        bufferedReader.close();
        bufferedWriter.close();
    }
}