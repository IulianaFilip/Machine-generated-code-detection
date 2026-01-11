import java.io.*;
import java.util.*;
import java.util.stream.*;
import static java.util.stream.Collectors.joining;
import static java.util.stream.Collectors.toList;

class Result {

    public static List<Integer> closestNumbers(List<Integer> arr) {
        List<Integer> closestPairs = new ArrayList<>();
        Collections.sort(arr);

        int minimumDifference = Integer.MAX_VALUE;

        for (int i = 1; i < arr.size(); i++) {
            int diff = arr.get(i) - arr.get(i - 1);

            if (diff < minimumDifference) {
                minimumDifference = diff;
                closestPairs.clear();
            }

            if (diff == minimumDifference) {
                closestPairs.add(arr.get(i - 1));
                closestPairs.add(arr.get(i));
            }
        }

        return closestPairs;
    }
}

public class Data6 {

    public static void main(String[] args) throws IOException {
        BufferedReader reader = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter writer = new BufferedWriter(
                new FileWriter(System.getenv("OUTPUT_PATH")));

        int n = Integer.parseInt(reader.readLine().trim());

        List<Integer> numbers = Stream.of(reader.readLine().trim().split("\\s+"))
                .map(Integer::parseInt)
                .collect(toList());

        List<Integer> result = Result.closestNumbers(numbers);

        writer.write(
                result.stream()
                        .map(Object::toString)
                        .collect(joining(" "))
                        + "\n");

        reader.close();
        writer.close();
    }
}
