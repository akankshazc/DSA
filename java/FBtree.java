/**
 * Check whether a binary tree is a full binary tree. A full binary tree is a
 * tree in which every node has either 0 or 2 children.
 */
class Node {
    int data;
    Node leftChild, rightChild;

    Node(int item) {
        data = item;
        leftChild = rightChild = null;
    }
}

class BinaryTree {
    Node root;

    /**
     * Determine whether the subtree rooted at {@code node} is a full binary
     * tree. The method is recursive and preserves the original algorithm.
     *
     * @param node subtree root (may be null)
     * @return true if the subtree is full, or if {@code node} is null
     */
    boolean isFullBinaryTree(Node node) {
        // An empty tree is considered full
        if (node == null) {
            return true;
        }

        // A leaf node is full
        if (node.leftChild == null && node.rightChild == null) {
            return true;
        }

        // If both left and right are non-null, check recursively
        if (node.leftChild != null && node.rightChild != null) {
            return isFullBinaryTree(node.leftChild) && isFullBinaryTree(node.rightChild);
        }

        // One child only -> not full
        return false;
    }

    /**
     * Convenience wrapper: check whether the whole tree (root) is full.
     */
    public boolean isFull() {
        return isFullBinaryTree(root);
    }

    public static void main(String args[]) {
        BinaryTree tree = new BinaryTree();
        tree.root = new Node(1);
        tree.root.leftChild = new Node(2);
        tree.root.rightChild = new Node(3);
        tree.root.leftChild.leftChild = new Node(4);
        tree.root.leftChild.rightChild = new Node(5);
        tree.root.rightChild.leftChild = new Node(6);
        tree.root.rightChild.rightChild = new Node(7);

        if (tree.isFull()) {
            System.out.print("The tree is a full binary tree");
        } else {
            System.out.print("The tree is not a full binary tree");
        }
    }
}