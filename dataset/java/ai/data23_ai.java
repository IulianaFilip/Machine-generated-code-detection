import java.io.*;
import java.util.*;
import java.util.stream.*;
import static java.util.stream.Collectors.toList;
import static java.util.stream.Collectors.joining;

class Result {

    public static List<Integer> countingSort(List<Integer> arr) {
        int MAX = 99;
        List<Integer> counts = new ArrayList<>(Collections.nCopies(MAX + 1, 0));

        for (int num : arr) {
            counts.set(num, counts.get(num) + 1);
        }

        return counts;
    }
}

public class Data23 {

    public static void main(String[] args) throws IOException {
        BufferedReader reader = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter writer = new BufferedWriter(
                new FileWriter(System.getenv("OUTPUT_PATH")));

        int n = Integer.parseInt(reader.readLine().trim());

        List<Integer> arr = Stream.of(reader.readLine().trim().split(" "))
                .map(Integer::parseInt)
                .collect(toList());

        List<Integer> result = Result.countingSort(arr);

        writer.write(
                result.stream()
                        .map(Object::toString)
                        .collect(joining(" "))
                        + "\n");

        reader.close();
        writer.close();
    }
}
