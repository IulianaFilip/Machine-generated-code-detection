import java.io.*;

class Result {

    public static String kangaroo(int x1, int v1, int x2, int v2) {
        int positionDiff = x1 - x2;
        int velocityDiff = v2 - v1;

        if (velocityDiff == 0 || positionDiff % velocityDiff != 0 || positionDiff / velocityDiff < 0) {
            return "NO";
        }

        return "YES";
    }
}

public class Data10 {

    public static void main(String[] args) throws IOException {
        BufferedReader reader = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter writer = new BufferedWriter(
                new FileWriter(System.getenv("OUTPUT_PATH")));

        String[] inputs = reader.readLine().trim().split(" ");
        int x1 = Integer.parseInt(inputs[0]);
        int v1 = Integer.parseInt(inputs[1]);
        int x2 = Integer.parseInt(inputs[2]);
        int v2 = Integer.parseInt(inputs[3]);

        String result = Result.kangaroo(x1, v1, x2, v2);

        writer.write(result);
        writer.newLine();

        reader.close();
        writer.close();
    }
}
