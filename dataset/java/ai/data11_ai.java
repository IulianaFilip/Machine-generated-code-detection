import java.io.*;
import java.util.*;
import java.util.stream.*;
import static java.util.stream.Collectors.joining;
import static java.util.stream.Collectors.toList;

class Result {

    public static List<Integer> rotateLeft(int d, List<Integer> arr) {
        int n = arr.size();
        List<Integer> rotated = new ArrayList<>(n);

        int startIndex = d % n;

        for (int i = startIndex; i < n; i++) {
            rotated.add(arr.get(i));
        }
        for (int i = 0; i < startIndex; i++) {
            rotated.add(arr.get(i));
        }

        return rotated;
    }
}

public class Data11 {

    public static void main(String[] args) throws IOException {
        BufferedReader reader = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter writer = new BufferedWriter(
                new FileWriter(System.getenv("OUTPUT_PATH")));

        String[] input = reader.readLine().trim().split(" ");
        int n = Integer.parseInt(input[0]);
        int d = Integer.parseInt(input[1]);

        List<Integer> arr = Stream.of(reader.readLine().trim().split(" "))
                .map(Integer::parseInt)
                .collect(toList());

        List<Integer> result = Result.rotateLeft(d, arr);

        writer.write(
                result.stream()
                        .map(Object::toString)
                        .collect(joining(" "))
                        + "\n");

        reader.close();
        writer.close();
    }
}
