import java.io.*;

class Result {

    public static int countingValleys(int steps, String path) {
        int valleys = 0;
        int level = 0;

        for (int i = 0; i < steps; i++) {
            char step = path.charAt(i);
            if (step == 'U') {
                level++;
                if (level == 0)
                    valleys++;
            } else if (step == 'D') {
                level--;
            }
        }

        return valleys;
    }
}

public class Data22 {

    public static void main(String[] args) throws IOException {
        BufferedReader reader = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter writer = new BufferedWriter(
                new FileWriter(System.getenv("OUTPUT_PATH")));

        int steps = Integer.parseInt(reader.readLine().trim());
        String path = reader.readLine();

        int result = Result.countingValleys(steps, path);

        writer.write(String.valueOf(result));
        writer.newLine();

        reader.close();
        writer.close();
    }
}
