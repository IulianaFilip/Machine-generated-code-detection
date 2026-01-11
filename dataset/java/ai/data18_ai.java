import java.io.*;
import java.util.*;
import java.util.stream.*;
import static java.util.stream.Collectors.toList;

class Result {

    public static String twoArrays(int k, List<Integer> A, List<Integer> B) {
        Collections.sort(A);
        Collections.sort(B, Collections.reverseOrder());

        for (int i = 0; i < A.size(); i++) {
            if (A.get(i) + B.get(i) < k) {
                return "NO";
            }
        }

        return "YES";
    }
}

public class Data18 {

    public static void main(String[] args) throws IOException {
        BufferedReader reader = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter writer = new BufferedWriter(
                new FileWriter(System.getenv("OUTPUT_PATH")));

        int q = Integer.parseInt(reader.readLine().trim());

        IntStream.range(0, q).forEach(i -> {
            try {
                String[] params = reader.readLine().trim().split(" ");
                int n = Integer.parseInt(params[0]);
                int k = Integer.parseInt(params[1]);

                List<Integer> A = Stream.of(reader.readLine().trim().split(" "))
                        .map(Integer::parseInt)
                        .collect(toList());

                List<Integer> B = Stream.of(reader.readLine().trim().split(" "))
                        .map(Integer::parseInt)
                        .collect(toList());

                String result = Result.twoArrays(k, A, B);

                writer.write(result);
                writer.newLine();
            } catch (IOException e) {
                throw new RuntimeException(e);
            }
        });

        reader.close();
        writer.close();
    }
}
