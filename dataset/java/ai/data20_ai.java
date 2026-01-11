import java.io.*;

class Result {

    public static int marsExploration(String s) {
        int count = 0;

        for (int i = 0; i < s.length(); i++) {
            char ch = s.charAt(i);

            if (i % 3 == 0 || i % 3 == 2) {
                if (ch != 'S')
                    count++;
            } else {
                if (ch != 'O')
                    count++;
            }
        }

        return count;
    }
}

public class Data20 {

    public static void main(String[] args) throws IOException {
        BufferedReader reader = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter writer = new BufferedWriter(
                new FileWriter(System.getenv("OUTPUT_PATH")));

        String s = reader.readLine();
        int result = Result.marsExploration(s);

        writer.write(String.valueOf(result));
        writer.newLine();

        reader.close();
        writer.close();
    }
}
