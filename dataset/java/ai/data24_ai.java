import java.io.*;
import java.util.*;

class Result {

    public static int divisibleSumPairs(int n, int k, List<Integer> ar) {
        int[] remainderCount = new int[k];
        int pairs = 0;

        for (int num : ar) {
            int remainder = num % k;
            int complement = (k - remainder) % k;
            pairs += remainderCount[complement];
            remainderCount[remainder]++;
        }

        return pairs;
    }
}

public class Data24 {

    public static void main(String[] args) throws IOException {
        BufferedReader reader = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter writer = new BufferedWriter(
                new FileWriter(System.getenv("OUTPUT_PATH")));

        String[] inputParams = reader.readLine().trim().split(" ");
        int n = Integer.parseInt(inputParams[0]);
        int k = Integer.parseInt(inputParams[1]);

        List<Integer> ar = new ArrayList<>();
        for (String s : reader.readLine().trim().split(" ")) {
            ar.add(Integer.parseInt(s));
        }

        int result = Result.divisibleSumPairs(n, k, ar);

        writer.write(String.valueOf(result));
        writer.newLine();

        reader.close();
        writer.close();
    }
}
