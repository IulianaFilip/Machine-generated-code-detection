import java.io.*;
import java.util.*;
import java.util.stream.*;
import static java.util.stream.Collectors.toList;

class Result {

    public static int pickingNumbers(List<Integer> numbers) {
        final int MAX_VALUE = 99;
        int[] frequency = new int[MAX_VALUE + 1];

        for (int num : numbers) {
            frequency[num]++;
        }

        int maxLength = 0;
        for (int i = 1; i < MAX_VALUE; i++) {
            int currentLength = frequency[i] + frequency[i + 1];
            maxLength = Math.max(maxLength, currentLength);
        }

        return maxLength;
    }
}

public class Data12 {

    public static void main(String[] args) throws IOException {
        BufferedReader reader = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter writer = new BufferedWriter(
                new FileWriter(System.getenv("OUTPUT_PATH")));

        int n = Integer.parseInt(reader.readLine().trim());

        List<Integer> numbers = Stream.of(reader.readLine().trim().split(" "))
                .map(Integer::parseInt)
                .collect(toList());

        int result = Result.pickingNumbers(numbers);

        writer.write(String.valueOf(result));
        writer.newLine();

        reader.close();
        writer.close();
    }
}
