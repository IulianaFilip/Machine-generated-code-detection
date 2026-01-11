import java.util.*;

public class Data16 {

    public static String stringsXOR(String s, String t) {
        StringBuilder result = new StringBuilder(s.length());

        for (int i = 0; i < s.length(); i++) {
            result.append(s.charAt(i) == t.charAt(i) ? '0' : '1');
        }

        return result.toString();
    }

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        String s = scanner.nextLine();
        String t = scanner.nextLine();

        System.out.println(stringsXOR(s, t));
        scanner.close();
    }
}
