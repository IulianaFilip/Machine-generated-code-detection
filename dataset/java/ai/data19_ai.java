import java.io.*;
import java.util.*;
import java.util.stream.*;
import static java.util.stream.Collectors.toList;

class Result {

    public static int flippingMatrix(List<List<Integer>> matrix) {
        int n = matrix.size() / 2;
        int maxSum = 0;

        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                int topLeft = matrix.get(i).get(j);
                int topRight = matrix.get(i).get(2 * n - 1 - j);
                int bottomLeft = matrix.get(2 * n - 1 - i).get(j);
                int bottomRight = matrix.get(2 * n - 1 - i).get(2 * n - 1 - j);

                maxSum += Math.max(Math.max(topLeft, topRight), Math.max(bottomLeft, bottomRight));
            }
        }

        return maxSum;
    }
}

public class Data19 {

    public static void main(String[] args) throws IOException {
        BufferedReader reader = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter writer = new BufferedWriter(
                new FileWriter(System.getenv("OUTPUT_PATH")));

        int q = Integer.parseInt(reader.readLine().trim());

        IntStream.range(0, q).forEach(query -> {
            try {
                int n = Integer.parseInt(reader.readLine().trim());

                List<List<Integer>> matrix = new ArrayList<>();

                IntStream.range(0, 2 * n).forEach(i -> {
                    try {
                        List<Integer> row = Stream.of(reader.readLine().trim().split(" "))
                                .map(Integer::parseInt)
                                .collect(toList());
                        matrix.add(row);
                    } catch (IOException e) {
                        throw new RuntimeException(e);
                    }
                });

                int result = Result.flippingMatrix(matrix);
                writer.write(String.valueOf(result));
                writer.newLine();

            } catch (IOException e) {
                throw new RuntimeException(e);
            }
        });

        reader.close();
        writer.close();
    }
}
