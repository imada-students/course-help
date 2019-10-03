import java.io.FileInputStream;
import java.io.FileOutputStream;
import java.io.OutputStream;

public class Encode {
    public static void main(String[] args) throws Exception {

        FileInputStream inFile = new FileInputStream(args[0]);
        FileOutputStream outFile = new FileOutputStream(args[1]);

        int[] amountOfBytes = new int[256];

        while (inFile.available() != 0) {
            int i = inFile.read(); // Save it so we don't read the next byte when adding 1.
            amountOfBytes[i] = amountOfBytes[i] + 1;
        }

        BitOutputStream outBit = new BitOutputStream(outFile);

        for (int i = 0; i < amountOfBytes.length; i++) {
            if (amountOfBytes[i] != 0)
                System.out.println(amountOfBytes[i]);
        }
        Element a = new Element(5, new Object());

        huffman(amountOfBytes);

    }

    private static PQ huffman(int[] amountOfBytes) {
        PQ test = new PQHeap(amountOfBytes.length);

        int n = amountOfBytes.length;
        for (int i = 0; i < n; i++) {
            test.insert(new Element(amountOfBytes[i], new Node(0)));
        }

        for (int i = 0; i < n - 1; i++) {
            Node node = new Node(0);
            node.leftNode = test.extractMin();
            node.rightNode = test.extractMin();
            node.key = node.leftNode.getKey() + node.rightNode.getKey();
            test.insert(new Element(node.key, node));
            if (node.key != 0)
                System.out.println("1. - Node.key: " + node.key + " Node.left: " + node.leftNode.getKey()
                        + " Node.right: " + node.rightNode.getKey());
        }
        return test;
    }

    private static class Node {
        private int key;
        private Element rightNode;
        private Element leftNode;
        private Element parentNode;

        private Node(int key) {
            this.key = key;
        }

    }

}
