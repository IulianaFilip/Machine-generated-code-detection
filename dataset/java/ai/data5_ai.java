import java.io.*;
import java.util.stream.*;
import static java.util.stream.Collectors.toList;

class Result {

    public static int towerBreakers(int n, int m) {
        // Player 2 wins if all towers have height 1
        if (m == 1) {
            return 2;
        }

        // Player 2 wins if number of towers is even
        if (n % 2 == 0) {
            return 2;
        }

        // Player 1 wins if number of towers is odd
        return 1;
    }
}

public class Data5 {

public static void main(String[] args) throws IOException {
        BufferedReader reader = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter writer = new BufferedWriter(
                new FileWriter(System.getenv("OUTPUT_PATH"))
        );

        int testCases = Integer.parseInt(reader.readLine().trim());

        IntStream.range(0, testCases).forEach(i -> {
            try {
                String[] inputs = reader.readLi
