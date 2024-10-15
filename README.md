public class CRCCCITT16 {

    private static final int POLYNOMIAL = 0x1021;  // CRC-CCITT polynomial
    private static final int CRC_INITIAL = 0xFFFF;  // Initial CRC value

    // Method to calculate CRC
    public static int calculateCRC(byte[] data) {
        int crc = CRC_INITIAL;
        for (byte b : data) {
            crc ^= (b << 8);  // XOR byte into top of 16-bit CRC
            for (int i = 0; i < 8; i++) {
                crc = (crc & 0x8000) != 0 ? (crc << 1) ^ POLYNOMIAL : crc << 1;  // Shift and XOR
            }
        }
        return crc & 0xFFFF;  // Return 16-bit result
    }

    public static void main(String[] args) {
        byte[] data = "Hello, CRC!".getBytes();  // Sample data
        int crc = calculateCRC(data);  // Calculate CRC
        System.out.printf("CRC-CCITT (16-bit): 0x%04X\n", crc);  // Output result
    }
}
