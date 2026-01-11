import java.io.*;
import java.util.*;
import java.util.stream.*;

import static java.util.stream.Collectors.toList;

class Result {

    public static int minimumAbsoluteDifference(List<Integer> arr) {
        Collections.sort(arr);

        int minimumDifference = Integer.MAX_VALUE;

        for (int index = 1; index < arr.size(); index++) {
            int currentDifference = arr.get(index) - arr.get(index - 1);
            minimumDifference = Math.min(minimumDifference, currentDifference);
        }

        return minimumDifference;
    }
}

public class Data4 {

    public static void main(String[] args) throws IOException {
        BufferedReader reader = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter writer = new BufferedWriter(
                new FileWriter(System.getenv("OUTPUT_PATH")));

        int n = Integer.parseInt(reader.readLine().trim());

        List<Integer> numbers = Stream.of(reader.readLine().trim().split("\\s+"))
                .map(Integer::parseInt)
                .collect(toList());

        int result = Result.minimumAbsoluteDifference(numbers);

        writer.write(Integer.toString(result));
        writer.newLine();

        reader.close();
        writer.close();
    }
}
