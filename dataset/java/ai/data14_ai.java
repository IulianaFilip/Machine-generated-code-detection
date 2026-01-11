import java.io.*;

class Result {

    public static int pageCount(int n, int p) {
        int fromLeft = p / 2;
        int fromRight = n / 2 - fromLeft;
        return Math.min(fromLeft, fromRight);
    }
}

public class Data14 {

    public static void main(String[] args) throws IOException {
        BufferedReader reader = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter writer = new BufferedWriter(
                new FileWriter(System.getenv("OUTPUT_PATH")));

        int n = Integer.parseInt(reader.readLine().trim());
        int p = Integer.parseInt(reader.readLine().trim());

        int result = Result.pageCount(n, p);

        writer.write(String.valueOf(result));
        writer.newLine();

        reader.close();
        writer.close();
    }
}
