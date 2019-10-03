public class Relations {

    /*
     * Takes a zero-one matrix (n x n) representing a relation and returns
     * the transitive closure of the relation using Warshall's algorithm.
     * Changes the original matrix.
     */
    public static int[][] getTransitiveClosure(int[][] relation) {
        int n = relation.length;
        int[][] W = relation;
        for (int k = 0; k < n; k++) {
            for (int i = 0; i < n; i++) {
                for (int j = 0; j < n; j++) {
                    W[i][j] = (W[i][j] == 1 || (W[i][k] == 1 && W[k][j] == 1)) ? 1 : 0;
                }
            }
        }
        return W;
    }

    /*
     * Takes a zero-one matrix (n x n) representing a relation and returns
     * the reflexive closure of the relation.
     * Changes the original relation.
     */
    public static int[][] getReflexiveClosure(int[][] relation) {
        int n = relation.length;
        int[][] reflexiveClosure = relation;
        for (int i = 0; i < n; i++) {
            reflexiveClosure[i][i] = 1;
        }
        return reflexiveClosure;
    }

    /*
     * Takes a zero-one matrix (n x n) representing a relation and returns
     * true if the relation is reflexive.
     */
    public static boolean isReflexive(int[][] relation) {
        int n = relation.length;
        for (int i = 0; i < n; i++) {
            if (relation[i][i] != 1) 
                return false;
        }
        return true;
    }

    /*
     * Takes a zero-one matrix (n x n) representing a relation
     * and returns true if the relation is symmetric.
     */
    public static boolean isSymmetric(int[][] relation) {
        int n = relation.length;
        for (int i = 1; i < n; i++) {
            for (int j = 0; j < i; j++) {
                if ((relation[i][j] == 1 || relation[j][i] == 1) && (relation[i][j] != 1 || relation[j][i] != 1)) //XOR
                    return false;
            }
        }
        return true;
    }

    /*
     * Converts a number to a letter. 0 is a, 1 is b and so forth
     * Assumes that number < 10
     */ 
    private static char numberToLetter(int number) {
        switch (number) {
            case 0: return 'a';
            case 1: return 'b';
            case 2: return 'c';
            case 3: return 'd';
            case 4: return 'e';
            case 5: return 'f';
            case 6: return 'g';
            case 7: return 'h';
            case 8: return 'i';
            case 9: return 'j';
            default: return '0';
        }
    }

    /*
     * Takes a zero-one matrix (n x n) representing a relation and prints
     * the ordered pairs in the relation
     */
    public static void printOrderedPairs(int[][] relation) {
        int n = relation.length;
        StringBuilder orderedPairs = new StringBuilder();
        orderedPairs.append("{");
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                if (relation[i][j] == 1) {
                    char a = numberToLetter(i);
                    char b = numberToLetter(j);
                    orderedPairs.append("(" + a + ", " + b + "), ");
                }
            }
        }
        //Delete the last comma and space
        orderedPairs.delete(orderedPairs.length()-2, orderedPairs.length());
        orderedPairs.append("}");
        System.out.println(orderedPairs.toString());
    }

    public static void main(String[] args) {
        int[][] relation = {
            {0, 0, 0, 1},
            {1, 0, 1, 0},
            {1, 0, 0, 1}, 
            {0, 0, 1, 0}
        };

        int[][] relation2 = {
            {1, 0, 1},
            {0, 1, 0},
            {1, 1, 0}
        };

        int[][] test = {
            {1, 1, 0, 0},
            {0, 0, 1, 0},
            {0, 0, 0, 1},
            {0, 0, 1, 0}
        };

        int[][] test2 = {
            {0, 1, 0, 0, 0},
            {1, 0, 1, 0, 0},
            {0, 0, 0, 1, 1},
            {0, 0, 0, 0, 0},
            {0, 0, 0, 0, 0}
        };

        printOrderedPairs(test2);
        printOrderedPairs(getTransitiveClosure(test2));
        // System.out.println(isSymmetric(test));
        // printOrderedPairs(test);
        // int[][] transitiveClosure = getTransitiveClosure(test);
        // printOrderedPairs(transitiveClosure);
    }
}