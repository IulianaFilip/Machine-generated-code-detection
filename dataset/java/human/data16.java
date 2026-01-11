import java.io.*;
import java.util.*;
import java.text.*;
import java.math.*;
import java.util.regex.*;

public class Data16 {
    public static String stringsXOR(String s, String t) {
        String res = new String("");

        for (int i = 0; i < s.length(); i++) {
            res += s.charAt(i) == t.charAt(i) ? "0" : "1";
        }

        return res;
    }

    public static void main(String[] args) {
        String s, t;

        Scanner in = new Scanner(System.in);
        s = in.nextLine();
        t = in.nextLine();

        System.out.println(stringsXOR(s, t));
    }
}
