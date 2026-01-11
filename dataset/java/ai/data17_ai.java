import java.io.*;
import java.util.*;
import java.util.stream.*;
import static java.util.stream.Collectors.toList;

class Result {

    public static int birthday(List<Integer> s, int d, int m) {
        int count = 0;

        int currentSum = 0;
        for (int i = 0; i < m; i++) {
            currentSum += s.get(i);
        }
        if (currentSum == d) {
            count++;
        }

        for (int i = m; i < s.size(); i++) {
            currentSum += s.get(i) - s.get(i - m);
            if (currentSum == d) {
                count++;
            }
        }

        return count;
    }
}

public class Data17 {

    public static void main(String[] args) throws IOException {
        BufferedReader reader = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter writer = new BufferedWriter(
                new FileWriter(System.getenv("OUTPUT_PATH")));

        int n = Integer.parseInt(reader.readLine().trim());

        List<Integer> s = Stream.of(reader.readLine().trim().split(" "))
                .map(Integer::parseInt)
                .collect(toList());

        String[] params = reader.readLine().trim().split(" ");
        int d = Integer.parseInt(params[0]);
        int m = Integer.parseInt(params[1]);

        int result = Result.birthday(s, d, m);

        writer.write(String.valueOf(result));
        writer.newLine();

        reader.close();
        writer.close();
    }
}
