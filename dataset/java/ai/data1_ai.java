import java.util.*;

class Result {

    public static String caesarCipher(String input, int shift) {
        final int ALPHABET_SIZE = 26;
        int normalizedShift = shift % ALPHABET_SIZE;

        StringBuilder encrypted = new StringBuilder(input.length());

        for (int index = 0; index < input.length(); index++) {
            char currentChar = input.charAt(index);

            if (currentChar >= 'A' && currentChar <= 'Z') {
                char shiftedChar = (char) ('A' + (currentChar - 'A' + normalizedShift) % ALPHABET_SIZE);
                encrypted.append(shiftedChar);
            } else if (currentChar >= 'a' && currentChar <= 'z') {
                char shiftedChar = (char) ('a' + (currentChar - 'a' + normalizedShift) % ALPHABET_SIZE);
                encrypted.append(shiftedChar);
            } else {
                encrypted.append(currentChar);
            }
        }

        return encrypted.toString();
    }
}
