import java.io.*;
import java.util.stream.IntStream;

class Result {

    public static void separateNumbers(String s) {
        int n = s.length();

        for (int i = 1; i <= n / 2; i++) {
            String firstNumStr = s.substring(0, i);
            long firstNum = Long.parseLong(firstNumStr);

            StringBuilder candidate = new StringBuilder(firstNumStr);
            long nextNum = firstNum;

            while (candidate.length() < n) {
                nextNum++;
                candidate.append(nextNum);
            }

            if (candidate.toString().equals(s)) {
                System.out.println("YES " + firstNumStr);
                return;
            }
        }

        System.out.println("NO");
    }
}

public class Data9 {

    public static void main(String[] args) throws IOException {
        BufferedReader reader = new BufferedReader(new InputStreamReader(System.in));

        int queries = Integer.parseInt(reader.readLine().trim());

        IntStream.range(0, queries).forEach(i -> {
            try {
                String s = reader.readLine();
                Result.separateNumbers(s);
            } catch (IOException e) {
                throw new RuntimeException(e);
            }
        });

        reader.close();
    }
}
