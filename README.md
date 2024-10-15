public class import java.util.*;

public class CRC {
    static String msg;
    static String genPoly = "110010";  // Generator polynomial
    static char t[] = new char[128];
    static char q[] = new char[128];
    static char cs[] = new char[128];
    static int mlen, glen, x, i, flag = 0, test;

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        // Step 1: Ask user to enter the message
        System.out.print("Enter the message: ");
        msg = sc.nextLine();
        mlen = msg.length();  // Store length of message
        System.out.println("Length of the message: " + mlen);

        // Step 2: Convert message to array of bits and store in t[]
        for (i = 0; i < mlen; i++) {
            t[i] = msg.charAt(i);  // Storing bits of message
        }
        System.out.print("Bits of the message (t[]): ");
        for (i = 0; i < mlen; i++) {
            System.out.print(t[i] + " ");
        }
        System.out.println();

        // Step 3: Convert genPoly to array of bits and store in q[]
        glen = genPoly.length();  // Store length of generator polynomial
        for (i = 0; i < glen; i++) {
            q[i] = genPoly.charAt(i);  // Storing bits of generator polynomial
        }
        System.out.print("Bits of the generator polynomial (q[]): ");
        for (i = 0; i < glen; i++) {
            System.out.print(q[i] + " ");
        }
        System.out.println();

        // Step 4: Append (glen - 1) zeros to t[]
        for (i = mlen; i < mlen + glen - 1; i++) {
            t[i] = '0';  // Appending zeros
        }
        System.out.print("Message after appending zeros (t[]): ");
        for (i = 0; i < mlen + glen - 1; i++) {
            System.out.print(t[i] + " ");
        }
        System.out.println();

        // Step 5: Perform division (CRC algorithm)
        for (i = 0; i < mlen; i++) {
            if (t[i] == '1') {
                for (x = 0; x < glen; x++) {
                    t[i + x] = xor(t[i + x], q[x]);  // XOR division
                }
            }
        }

        // Step 6: Store the remainder (CRC) in cs[]
        for (i = mlen; i < mlen + glen - 1; i++) {
            cs[i - mlen] = t[i];  // Remainder (CRC)
        }

        // Display the CRC code
        System.out.print("CRC (remainder): ");
        for (i = 0; i < glen - 1; i++) {
            System.out.print(cs[i] + " ");
        }
        System.out.println();

        // Final codeword (message + CRC)
        System.out.print("Final codeword (message + CRC): ");
        for (i = 0; i < mlen; i++) {
            System.out.print(msg.charAt(i) + " ");
        }
        for (i = 0; i < glen - 1; i++) {
            System.out.print(cs[i] + " ");
        }
        System.out.println();
    }

    // XOR function
    public static char xor(char a, char b) {
        return (a == b) ? '0' : '1';
    }

}
