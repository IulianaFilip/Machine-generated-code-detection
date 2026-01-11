import java.io.*;
import java.util.*;

class Result {

    public static List<Integer> matchingStrings(List<String> strings, List<String> queries) {
        Map<String, Integer> counts = new HashMap<>();

        for (String str : strings) {
            counts.put(str, counts.getOrDefault(str, 0) + 1);
        }

        List<Integer> result = new ArrayList<>();
        for (String query : queries) {
            result.add(counts.getOrDefault(query, 0));
        }

        return result;
    }
}

public class Data25 {

    public static void main(String[] args) throws IOException {
        BufferedReader reader = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter writer = new BufferedWriter(
                new FileWriter(System.getenv("OUTPUT_PATH")));

        int stringsCount = Integer.parseInt(reader.readLine().trim());
        List<String> strings = new ArrayList<>();
        for (int i = 0; i < stringsCount; i++) {
            strings.add(reader.readLine());
        }

        int queriesCount = Integer.parseInt(reader.readLine().trim());
        List<String> queries = new ArrayList<>();
        for (int i = 0; i < queriesCount; i++) {
            queries.add(reader.readLine());
        }

        List<Integer> res = Result.matchingStrings(strings, queries);

        for (int i = 0; i < res.size(); i++) {
            writer.write(String.valueOf(res.get(i)));
            if (i < res.size() - 1)
                writer.write("\n");
        }
        writer.newLine();

        reader.close();
        writer.close();
    }
}
