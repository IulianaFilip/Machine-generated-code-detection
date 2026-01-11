import java.io.*;

class Result {

    public static String pangrams(String s) {
        boolean[] used = new boolean[26];

        for (int i = 0; i < s.length(); i++) {
            char ch = s.charAt(i);
            if (Character.isLetter(ch)) {
                int index = Character.toUpperCase(ch) - 'A';
                used[index] = true;
            }
        }

        for (boolean b : used) {
            if (!b)
                return "not pangram";
        }

        return "pangram";
    }
}

public class Data21 {

    public static void main(String[] args) throws IOException {
        BufferedReader reader = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter writer = new BufferedWriter(
                new FileWriter(System.getenv("OUTPUT_PATH")));

        String s = reader.readLine();
        String result = Result.pangrams(s);

        writer.write(result);
        writer.newLine();

        reader.close();
        writer.close();
    }
}
