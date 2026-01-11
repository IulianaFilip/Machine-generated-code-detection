import java.io.*;
import java.util.*;
import java.util.stream.*;
import static java.util.stream.Collectors.toList;
import static java.util.stream.Collectors.joining;

class Result {

    public static List<Integer> maximumPerimeterTriangle(List<Integer> sticks) {
        Collections.sort(sticks, Collections.reverseOrder());

        for (int i = 0; i < sticks.size() - 2; i++) {
            int a = sticks.get(i);
            int b = sticks.get(i + 1);
            int c = sticks.get(i + 2);

            if (b + c > a) {
                return Arrays.asList(c, b, a);
            }
        }

        return Arrays.asList(-1);
    }
}

public class Data15 {

public static void main(String[] args) throws IOException {
        BufferedReader reader = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter
