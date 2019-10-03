/*
 * Implements ordered, binary trees.
 * The elements must be comparable.
 */
public class BinaryTree<E extends Comparable<E>> implements MyCollection<E> {
    /*
     * Implementation of a node in a binary tree.
     */
    private static class Node<T extends Comparable<T>> {
        private final int SPACES = 3;
        private Node<T> left;
        private Node<T> right;
        private T value;

        /*
         * Creates a new node with the given value.
         */
        public Node(Node<T> left, Node<T> right, T value) {
            this.left = left;
            this.right = right;
            this.value = value;
        }

        /*
         * Adds an element to the tree of nodes starting
         * from this node such that the tree is ordered.
         */
        public void add(T t) {
            if (t.compareTo(this.value) < 0) {
                if (this.left == null)
                    this.left = new Node(null, null, t);
                else
                    this.left.add(t);
            }
            else if (this.right == null)
                this.right = new Node(null, null, t);
            else
                this.right.add(t);
        }

        /*
         * Prints the tree with this node as root.
         */
        public void printTree(int spaces) {
            if (this.right != null)
                this.right.printTree(spaces + SPACES);
            for (int i = 0; i < spaces; i++)
                System.out.print(" ");
            System.out.print(this.value + "\n");
            if (this.left != null)
                this.left.printTree(spaces + SPACES);
        }

        /*
         * Returns true if the tree with this node
         * as root contains e
         */
        public boolean contains(T t) {
            if (this.value.equals(t))
                return true;
            else if (t.compareTo(this.value) < 0)
                return ((this.left != null) && this.left.contains(t));
            else
                return ((this.right != null) && this.right.contains(t));
        }

        /*
         * Returns the number of nodes in the
         * tree with this node as root.
         */
        public int size() {
            int size = 0;
            if (this.right != null)
                size += this.right.size();
            size++;
            if (this.left != null)
                size += this.left.size();
            return size;
        }

        /*
         * Returns the longest path from this node
         * to a leaf node.
         */
        public int height() {
            int height = 0;
            if (this.right != null)
                height = 1 + this.right.height();
            if (this.left != null)
                height = Math.max(height, 1 + this.left.height());
            return height;
        }

        /*
         * Transforms the tree with this node as its root
         * into its mirror image - every node's left child 
         * becomes its right child and vice-versa.
         */
        public void mirror() {
            if ((this.right != null) || (this.left != null)) {
                if (this.right != null)
                    this.right.mirror();
                if (this.left != null)
                    this.left.mirror();
                Node<T> temp = this.right;
                this.right = this.left;
                this.left = temp;
            }
        }
    }

    /*
     * Inner class implementing the Iterator<E> interface as a 
     * post-order traversal.
     * The implementation destroys the original nodes, so we 
     * must copy them.
     */
    private class PostOrderIterator implements Iterator<E> {
        private Stack<Node<E>> nextNodes;

        public PostOrderIterator() {
            nextNodes = new Stack<Node<E>>();
            if (root != null)
                nextNodes.add(Node.copy(root));
        }

        public boolean hasNext() {
            return this.nextNodes.isEmpty();
        }

        public E next() {
            return null; // TO DO
        }
    }

    private Node<E> root;

    /*
     * Creates a new binary tree with the
     * given node as root.
     */
    private BinaryTree(Node<E> root) {
        this.root = root;
    }

    /*
     * Creates a new, empty binary tree.
     */
    public BinaryTree() {
        this(null);
    }

    /*
     * Adds an element to this binary tree such
     * that this binary tree remains ordered.
     */
    public void add(E e) {
        if (this.root == null)
            this.root = new Node(null, null, e);
        else 
            this.root.add(e);
    }

    /*
     * Removes all elements in this binary tree.
     */
    public void clear() {
        this.root = null;
    }

    /*
     * Returns true if this binary tree contains
     * e.
     */
    public boolean contains(E e) {
        return this.root.contains(e);
    }

    /*
     * Returns true if this binary tree is empty.
     */
    public boolean isEmpty() {
        return (this.root == null);
    }

    /*
     * Returns the number of elements in this
     * binary tree.
     */
    public int size() {
        return this.root.size();
    }

    /*
     * Returns the element at the root node of
     * this binary tree.
     */
    public E root() {
        return this.root.value;
    }

    /*
     * Returns the subtree with the left
     * child of the current root node as root.
     */
    public BinaryTree<E> left() {
        if (this.root.left == null)
            return new BinaryTree();
        else
            return new BinaryTree(this.root.left);
    }

    /*
     * Returns the subtree with the right
     * child of the current root node as root.
     */
    public BinaryTree<E> right() {
        if (this.root.right == null)
            return new BinaryTree();
        else
            return new BinaryTree(this.root.right);
    }

    /*
     * Returns the longest path from the root
     * to a leaf node.
     */
    public int height() {
        return this.root.height();
    }

    /*
     * Transforms t into its mirror image - every
     * node's left child becomes its right child
     * and vice-versa.
     */
    public static void mirror(BinaryTree t) {
        t.root.mirror();
    }

    /*
     * Prints a representation of this tree.
     */
    public void printTree() {
        this.root.printTree(0);
    }
}